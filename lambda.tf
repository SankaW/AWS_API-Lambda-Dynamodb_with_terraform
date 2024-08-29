# Data sources to get current account ID and API Gateway information
data "aws_caller_identity" "current" {}

# data "aws_api_gateway_rest_api" "warehouse_api" {
#   name = var.api_name
# }

resource "aws_lambda_function" "get_all_data" {
  function_name = var.lambda_function_name
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  role = aws_iam_role.lambda_exec_role.arn

  filename      = "lambda_functions/get_all_data.zip"
  source_code_hash = filebase64sha256("lambda_functions/get_all_data.zip")

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.warehouse_robot_logs.name
    }
  }
}

resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
      },
    ],
  })
}

resource "aws_iam_policy" "lambda_dynamodb_policy" {
  name = "lambda_dynamodb_policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "dynamodb:Scan",
        ],
        Effect   = "Allow",
        Resource = aws_dynamodb_table.warehouse_robot_logs.arn,
      },
    ],
  })
}

resource "aws_iam_role_policy_attachment" "lambda_exec_policy_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_dynamodb_policy.arn
}

# Ensure Correct Permissions for API Gateway
resource "aws_lambda_permission" "api_gateway_invoke" {
  statement_id  = "AllowAPIGatewayInvoke"  # Unique ID for the permission statement
  action        = "lambda:InvokeFunction"  # Action to allow invoking the Lambda function
  function_name = aws_lambda_function.get_all_data.arn  # Reference to the Lambda function ARN
  principal     = "apigateway.amazonaws.com"  # Principal that is allowed to invoke the function

  # Source ARN to limit the permission to a specific API Gateway
  source_arn    = "arn:aws:execute-api:${var.aws_region}:${data.aws_caller_identity.current.account_id}:${aws_api_gateway_rest_api.warehouse_api.id}/*"
}