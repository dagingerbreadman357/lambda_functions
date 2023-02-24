import json
import boto3
import dateutil

from datetime import datetime, timezone


def lambda_handler(event, context):
    # setting sqs as the resource
    sqs = boto3.resource('sqs')
    # obtain date and time in Pacific Standard Time
    local = datetime.now(dateutil.tz.gettz('US/Pacific'))
    # local time
    time = local.strftime('%I:%M%p on %B %d, %Y')
    # enter the URL of queue
    queue = sqs.Queue(
        url='https://sqs.us-west-2.amazonaws.com/026023833752/KingSQS_Time')

    # will send a message to queue with current time and date in PST
    queue.send_message(MessageBody=time)

    return {
        'statusCode': 200,
        # output will be local time
        'body': json.dumps(local.strftime('%I:%M%p on %B %d, %Y'), default=str)}
