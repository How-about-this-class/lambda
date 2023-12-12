import boto3
import json
from datetime import datetime

class DatabaseAccess():
    def __init__(self, TABLE_NAME):
        # DynamoDB 세팅
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(TABLE_NAME)

    def put_data(self, input_data):
        self.table.put_item(
            Item =  input_data
        )
        print("Putting data is completed!")
    def get_data(self, uk):
        res = self.table.get_item(Key={
            "uk": uk
          })
        items = res['Item'] # 모든 item
        return items

def lambda_handler(event, context):
    
    db_access = DatabaseAccess('inha_001_Review')
    
    # if event['requestContext']['http']['method'] == 'POST':
    #    input_data = {
    #        "uk" : int(event["uk"])
    #    }
    #    db_access.put_data(input_data)
    
    if event['httpMethod'] == 'GET':
        items = db_access.get_data(int(event['queryStringParameters']['uk']))
        
        print(event)
        
        del items['uk']
        return {
            'statusCode': 200,
            'body': json.dumps(items, ensure_ascii = False)
        }
        # print(f"items: {items}")

    else:
        print("Confirm the method!")
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('This is Hey Tech Blog!')
    }
