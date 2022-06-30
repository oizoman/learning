@description('The Azure region into which the resources should be deployed.')
param location string

@secure()
@description('The administrator login username for the SQL server.')
param sqlServerAdministratorLogin string

@secure()
@description('The administrator login password for the SQL server.')
param sqlServerAdministratorLoginPassword string

param sqlDatabaseSku object={
  name: 'Standard'
  tier: 'Standard'
}

@allowed([
  'Development'
  'Production'
])
@description('The name of the environment. This must be Development or Production.')
param environmentName string = 'Development'

@description('The name of the audit storage account SKU.')
param auditStorageAccountSkuName string = 'Standard_LRS'

var sqlServerName = 'teddy${location}${uniqueString(resourceGroup().id)}'
var sqlDatabaseName = 'Teddybear'
var auditingEnabled = environmentName == 'Production'
var auditStorageAccountName = take('bearaudit${location}${uniqueString(resourceGroup().id)}',24)

resource sqlServer 'Microsoft.Sql/servers@2021-11-01-preview'={
  location: location
  name: sqlServerName
  properties:{
    administratorLogin: sqlServerAdministratorLogin
    administratorLoginPassword: sqlServerAdministratorLoginPassword
  }
}

resource sqlDatabase 'Microsoft.Sql/servers/databases@2021-11-01-preview'={
  parent: sqlServer
  location: location
  name: sqlDatabaseName
  sku:sqlDatabaseSku
}

resource auditStorageAccount 'Microsoft.Storage/storageAccounts@2021-02-01'={
  kind: 'StorageV2'
  location: location
  name: auditStorageAccountName
  sku: {
    name:auditStorageAccountSkuName
  }
}

resource sqlServerAudit 'Microsoft.Sql/servers/auditingSettings@2021-11-01-preview'= if(auditingEnabled){
  parent:sqlServer
  name:'default'
  properties:{
    state:'Enabled'
    storageEndpoint: environmentName == 'Production' ? auditStorageAccount.properties.primaryEndpoints.blob : ''
    storageAccountAccessKey: environmentName == 'Production' ? listKeys(auditStorageAccount.id, auditStorageAccount.apiVersion).keys[0].value: ''
  }
}

output serverName string = sqlServer.name
output location string = location
output serverFullyQualifiedDomainName string = sqlServer.properties.fullyQualifiedDomainName
