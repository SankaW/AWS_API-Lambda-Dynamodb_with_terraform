# # Output the API Gateway invoke URL
# output "api_invoke_url" {
#   value = "${aws_api_gateway_deployment.warehouse_api_deployment.invoke_url}"
#   description = "The invoke URL of the API Gateway"
# }

# # Output the API key
# output "api_key_value" {
#   value       = aws_api_gateway_api_key.api_key.value
#   description = "The API key to access the API Gateway"
#   sensitive   = true  # Marking as sensitive to hide from default output
# }