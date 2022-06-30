param location string = 'eastus'
param storageAccountName string = 'toylaunch${uniqueString(resourceGroup().id)}'
param appServiceAppName string = 'toylaunch${uniqueString(resourceGroup().id)}'

@allowed([
  'nonprod'
  'prod'
])
param environmentType string

var storageAccountSkuName = (environmentType == 'prod') ? 'Standard_GRS' : 'Standard_LRS'


resource storageAccount 'Microsoft.Storage/storageAccounts@2021-08-01'={
  kind:'StorageV2'
  location: location
  name: storageAccountName
  sku: {
    name: storageAccountSkuName
  }
  properties:{
    accessTier:'Hot'
  }
}

module appService 'modules/appService.bicep' = {
  name: 'appService'
  params: {
    location: location
    appServiceAppName: appServiceAppName
    environmentType: environmentType
  }
}

output appServiceAppHostName string = appService.outputs.appServiceAppHostName
