################ Infrastructure Provider Info ######################

# Define the required providers
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

# Configure the AWS provider with the specified region
provider "aws" {
  region  = var.aws_region  
}