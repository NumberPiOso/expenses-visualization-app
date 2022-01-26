#!/bin/sh

# Following https://docs.microsoft.com/en-us/azure/container-instances/tutorial-docker-compose  

# Run from the root of the project

# app_name="TestFastAPIdeployFree"


resource_group="resourceGroupTest"
# location="eastus"
# acr_name="acrexptest"

# az group create --location $location \
#                 --name $resource_group


# az acr create --resource-group $resource_group\
#               --name $acr_name \
#               --sku Basic

# az acr login --name $acr_name
# az acr login --name acrexptest


# az acr repository show --name acrexptest --repository acrexptest.azurecr.io/expenses-front:v1
# az acr repository show --name acrexptest --repository acrexptest.azurecr.io/expenses-back:v1



# # Clean up
# # Delete resource ggroup
# az group delete -n $resource_group

# az group delete -n resourceGroupTest
