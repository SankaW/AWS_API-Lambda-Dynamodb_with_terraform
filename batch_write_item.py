import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Your table name
table_name = "WarehouseRobotLogs"

# Batch write data to DynamoDB
response = dynamodb.batch_write_item(
    RequestItems={
        table_name: [
            {
                "PutRequest": {
                    "Item": {
                        "timestamp": {"S": "1724674600"},
                        "log_id": {"S": "1"},
                        "robot_id": {"S": "RW-001"},
                        "power_source": {"S": "battery"},
                        "battery_voltage": {"N": "12.7"},
                        "battery_capacity": {"N": "98.0"},
                        "battery_type": {"S": "Li-ion"},
                        "battery_manufacturer": {"S": "ManufacturerA"},
                        "temperature_celsius": {"N": "22.5"},
                        "status": {"S": "active"},
                        "task_id": {"S": "TASK-1001"}
                    }
                }
            },
            {
                "PutRequest": {
                    "Item": {
                        "timestamp": {"S": "1724674610"},
                        "log_id": {"S": "2"},
                        "robot_id": {"S": "RW-002"},
                        "power_source": {"S": "grid"},
                        "battery_voltage": {"N": "230.0"},
                        "battery_capacity": {"N": "100.0"},
                        "battery_type": {"S": "N/A"},
                        "battery_manufacturer": {"S": "N/A"},
                        "temperature_celsius": {"N": "21.0"},
                        "status": {"S": "idle"},
                        "task_id": {"S": "TASK-1002"}
                    }
                }
            },
            {
                "PutRequest": {
                    "Item": {
                        "timestamp": {"S": "1724674620"},
                        "log_id": {"S": "3"},
                        "robot_id": {"S": "RW-003"},
                        "power_source": {"S": "battery"},
                        "battery_voltage": {"N": "11.9"},
                        "battery_capacity": {"N": "75.0"},
                        "battery_type": {"S": "NiMH"},
                        "battery_manufacturer": {"S": "ManufacturerB"},
                        "temperature_celsius": {"N": "23.0"},
                        "status": {"S": "charging"},
                        "task_id": {"S": "TASK-1003"}
                    }
                }
            }
        ]
    }
)

print("Batch write response:", response)
