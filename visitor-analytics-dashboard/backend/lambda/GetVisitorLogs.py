import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorLogs')

def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response.get('Items', [])
        sorted_items = sorted(items, key=lambda x: x['timestamp'], reverse=True)
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(sorted_items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
