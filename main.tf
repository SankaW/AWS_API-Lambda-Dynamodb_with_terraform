################ Register application ######################

# Register application
resource "aws_servicecatalogappregistry_application" "AWS_API_Lambda_Dynamodb" {
  name        = "AWSAPILambdaDynamodb"
  description = "Register AWS_API,Lambda,Dynamodb in the Cloud account"
}
