import json
import boto3
import os

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        return get_log_by_id(event)
    elif http_method == 'POST':
        return post_log(event)
    elif http_method == 'DELETE':
        return delete_log(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method Not Allowed'})
        }

def get_log_by_id(event):
    log_id = event['pathParameters']['id']
    try:
        response = table.get_item(Key={'log_id': log_id})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Log not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def post_log(event):
    try:
        log_data = json.loads(event['body'])
        table.put_item(Item=log_data)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Log created successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def delete_log(event):
    log_id = event['pathParameters']['id']
    try:
        response = table.delete_item(Key={'log_id': log_id})
        return {
            'statusCode': 204
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
