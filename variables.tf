variable "aws_region" {
  description = "AWS Region"
  type = string
}

variable "dynamodb_table_name" {
  description = "Name of the dynamodb_table"
  type = string
}

variable "api_name" {
  description = "Name of the API"
  type = string
}

variable "lambda_function_name" {
  description = "Name of the lambda function"
  type = string
}