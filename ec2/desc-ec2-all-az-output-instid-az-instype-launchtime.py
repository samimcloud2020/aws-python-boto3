import boto3
import time
from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))
client = boto3.client('ec2')


resp2 = client.describe_instances(Filters=[
        {
            'Name': 'availability-zone',
            'Values': [
                'us-east-1a', 'us-east-1b', 'us-east-1c', 'us-east-1d', 'us-east-1f'
            ]
        },


    ])
for x in resp2['Reservations']:
    for y in x['Instances']:
        print('the instance id is {} and instance state  {} & AZ is {} & inst Type is {} & launch time {}'.format(y['InstanceId'],y['State']['Name'],y['Placement']['AvailabilityZone'],y['InstanceType'],y['LaunchTime']))

