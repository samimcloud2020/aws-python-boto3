import boto3
client = boto3.client('ec2')


resp2 = client.describe_instances()
for x in resp2['Reservations']:
    for y in x['Instances']:
        print('the instance id is {} and instance state  {}'.format(y['InstanceId'],y['State']['Name']))
