################ Register application ######################

# Register application
resource "aws_servicecatalogappregistry_application" "API_Lambda_Dynamodb_AWS" {
  name        = "LambdaDynamodbAWSAPI"
  description = "Register AWS_API,Lambda,Dynamodb in the Cloud account"
}
