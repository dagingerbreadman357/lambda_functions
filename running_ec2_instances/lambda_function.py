import json
import boto3

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2')
    
    running_ids = []

    response = ec2.describe_instances()
    
    reservations = response['Reservations']
    
    for reservation in reservations:
        instances = reservation['Instances']
    
        for instance in instances:
            if ('running' in instance['State']['Name']):
                print(instance['InstanceId'])
                running_ids.append(instance['InstanceId'])
    
    return {
        'statusCode': 200,
        'body': json.dumps(running_ids)
    }