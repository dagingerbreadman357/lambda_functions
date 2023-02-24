import json
import boto3
import dateutil

from datetime import datetime, timezone


def lambda_handler(event, context):

    sqs = boto3.resource('sqs')                                                     # setting sqs as the resource    
    local = datetime.now(dateutil.tz.gettz('US/Pacific'))                           # obtain date and time in Pacific Standard Time    
    time = local.strftime('%I:%M%p on %B %d, %Y')                                   # local time    
    queue = sqs.Queue(
        url='https://sqs.us-west-2.amazonaws.com/026023833752/KingSQS_Time')        # enter the URL of queue
    
    queue.send_message(MessageBody=time)                                            # will send a message to queue with current time and date in PST

    return {
        'statusCode': 200,
        # output will be local time
        'body': json.dumps(local.strftime('%I:%M%p on %B %d, %Y'), default=str)}
