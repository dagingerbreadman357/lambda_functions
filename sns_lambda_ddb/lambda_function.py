import json
import boto3

def lambda_handler(event, context):
    ddb = boto3.client('dynamodb')

    for record in event['Records']:
        ddb_data = {}
        for k, v in record['Sns'].items():
            if(v == None or v == {}):
                continue
            print(k, v)
            ddb_data[k] = {'S': v}
            
        response = ddb.put_item(
            Item=ddb_data,
            TableName='lambda_sns',
        )
        print(response)