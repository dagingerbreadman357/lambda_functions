import json
import boto3
from datetime import datetime


def lambda_handler(event, context):  # required
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")

    sqs = boto3.client('sqs')  # client is required to interact with
    sqs.send_message(
        QueueUrl="https://sqs.us-west-2.amazonaws.com/026023833752/KingSQS_Time",
        MessageBody=current_time
    )

    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
