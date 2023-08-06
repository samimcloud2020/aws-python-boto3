import boto3


client = boto3.client('ec2')

def lambda_handler(event, context):
    x = client.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ])
    
    
    for a in x['Reservations']:
        print(type(a))
        for b in a['Instances']:
            print(type(b))
            print(b['InstanceId'],b['State']['Name'],b['InstanceType'])
            start = client.start_instances(InstanceIds=[b['InstanceId']])
            print(start)
            
    
