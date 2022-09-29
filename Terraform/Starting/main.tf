terraform {
  required_version = ">= 1.1"

  required_providers {
    aws = {
        version = ">= 3.50"
        source = "hashicorp/terraform-provider-aws"
    }
    azurerm = {
        version = ">= 3.24"
        source = "hashicorp/terraform-provider-azurerm"
    }
  }
}