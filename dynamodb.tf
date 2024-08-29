resource "aws_dynamodb_table" "warehouse_robot_logs" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "timestamp"
  range_key      = "log_id"

  attribute {
    name = "timestamp"
    type = "S"
  }

  attribute {
    name = "log_id"
    type = "S"
  }

  global_secondary_index {
    name            = "RobotIdIndex"
    hash_key        = "robot_id"
    projection_type = "ALL"
  }

  attribute {
    name = "robot_id"
    type = "S"
  }

  tags = {
    Environment = "production"
    Project     = "WarehouseRobot"
  }
}
