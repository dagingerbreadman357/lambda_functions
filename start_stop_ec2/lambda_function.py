import boto3


def lambda_handler(event, context):

    # Get list of Regions
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])

        # Stop the instances
        for instance in instances:
            instance.stop()                            # can be changed to instance.start
            print('Stopped instance: ', instance.id)
