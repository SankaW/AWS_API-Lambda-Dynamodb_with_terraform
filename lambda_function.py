import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

# Custom JSON encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            # Convert Decimal to float for JSON serialization
            return float(o)
        return super(DecimalEncoder, self).default(o)
        
def convert_float_to_decimal(item):
    """Recursively convert float to Decimal in the item dict."""
    if isinstance(item, list):
        return [convert_float_to_decimal(i) for i in item]
    elif isinstance(item, dict):
        return {k: convert_float_to_decimal(v) for k, v in item.items()}
    elif isinstance(item, float):
        return Decimal(str(item))
    else:
        return item

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        path_parameters = event.get('pathParameters')
        if path_parameters and 'id' in path_parameters:
            # Get one item by id from DynamoDB
            item_id = path_parameters['id']
            response = table.get_item(Key={'id': item_id})
            item = response.get('Item')
            if item:
                return {
                    'statusCode': 200,
                    'body': json.dumps(item, cls=DecimalEncoder)  # Use the custom DecimalEncoder
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Item not found'})
                }
        else:
            # Get all items from DynamoDB
            response = table.scan()
            items = response.get('Items', [])
            return {
                'statusCode': 200,
                'body': json.dumps(items, cls=DecimalEncoder, indent=2)  # Pretty-print JSON using DecimalEncoder
            }
    
    elif http_method == 'POST':
        # Add a new item to DynamoDB
        body = event.get('body')
        if body:
            item = json.loads(body)
            item = convert_float_to_decimal(item)  # Convert floats to Decimals
            try:
                table.put_item(Item=item)
                return {
                    'statusCode': 201,
                    'body': json.dumps({'message': 'Item created successfully'})
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps({'message': str(e)})
                }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid input'})
            }
    
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }
