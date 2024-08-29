import json
import boto3
import os
from decimal import Decimal  # Ensure this import is present

# Correctly set the table name
table_name = os.environ.get('DYNAMODB_TABLE', 'WarehouseRobotLogs')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(table_name)

# Custom JSON encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            # Convert Decimal to float for JSON serialization
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        # Scan the entire DynamoDB table
        response = table.scan()
        data = response.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(data, cls=DecimalEncoder)  # Use the custom encoder here
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }



