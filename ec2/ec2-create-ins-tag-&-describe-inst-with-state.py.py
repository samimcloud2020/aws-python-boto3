import boto3
client = boto3.client('ec2')
resp1 = client.run_instances(InstanceType='t2.micro',  MaxCount=2, MinCount=2, ImageId='ami-052efd3df9dad4825',
                             TagSpecifications=[
                                 {
                                     'ResourceType': 'instance',
                                     'Tags': [
                                         {
                                             'Key': 'name',
                                             'Value': 'prod'
                                         },
                                     ]
                                 },
                             ])


for x in resp1['Instances']:
    print(x['InstanceId'])
    print(x)

print ("Start : %s" % time.ctime())
time.sleep( 60 )
print ("End : %s" % time.ctime())

import boto3
client = boto3.client('ec2')


resp2 = client.describe_instances()
for x in resp2['Reservations']:
    for y in x['Instances']:
        print('the instance id are {}'.format(y['InstanceId']))
        print('the instance state are {}'.format(y['State']['Name']))
