# API Gateway REST API
resource "aws_api_gateway_rest_api" "warehouse_api" {
  name        = var.api_name
  description = "API to interact with DynamoDB for Warehouse Robot logs"
}

# API Gateway Resource (e.g., /logs)
resource "aws_api_gateway_resource" "warehouse_resource" {
  rest_api_id = aws_api_gateway_rest_api.warehouse_api.id
  parent_id   = aws_api_gateway_rest_api.warehouse_api.root_resource_id
  path_part   = "logs"
}

# GET Method Integration
resource "aws_api_gateway_method" "get_method" {
  rest_api_id   = aws_api_gateway_rest_api.warehouse_api.id
  resource_id   = aws_api_gateway_resource.warehouse_resource.id
  http_method   = "GET"
  authorization = "NONE"
  api_key_required = true
}

resource "aws_api_gateway_integration" "get_integration" {
  rest_api_id             = aws_api_gateway_rest_api.warehouse_api.id
  resource_id             = aws_api_gateway_resource.warehouse_resource.id
  http_method             = aws_api_gateway_method.get_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.get_all_data.invoke_arn
}

# Deploy API Gateway
resource "aws_api_gateway_deployment" "warehouse_api_deployment" {
  depends_on = [aws_api_gateway_integration.get_integration]
  rest_api_id = aws_api_gateway_rest_api.warehouse_api.id
  stage_name  = "prod"
}

# API Key
resource "aws_api_gateway_api_key" "warehouse_api_key" {
  name    = "WarehouseRobotAPIKey"
  enabled = true
}

# Usage Plan for API Key
resource "aws_api_gateway_usage_plan" "warehouse_usage_plan" {
  name = "WarehouseUsagePlan"

  api_stages {
    api_id = aws_api_gateway_rest_api.warehouse_api.id
    stage  = aws_api_gateway_deployment.warehouse_api_deployment.stage_name
  }

  throttle_settings {
    burst_limit = 100
    rate_limit  = 50
  }
}

# Link API Key with Usage Plan
resource "aws_api_gateway_usage_plan_key" "warehouse_usage_plan_key" {
  key_id        = aws_api_gateway_api_key.warehouse_api_key.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.warehouse_usage_plan.id
}