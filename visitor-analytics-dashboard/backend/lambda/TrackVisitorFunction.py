import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorLogs')

def lambda_handler(event, context):
    print("Event received:", event)
    try:
        body = json.loads(event.get('body', '{}'))
        user_agent = body.get('userAgent')
        timestamp = body.get('timestamp')
        platform = body.get('platform')
        language = body.get('language')
        visitor_id = str(uuid.uuid4())
        table.put_item(Item={
            'visitorId': visitor_id,
            'timestamp': timestamp,
            'userAgent': user_agent,
            'platform': platform,
            'language': language
        })
        print("✅ Visitor data saved to DynamoDB.")
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Visitor data received'})
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
