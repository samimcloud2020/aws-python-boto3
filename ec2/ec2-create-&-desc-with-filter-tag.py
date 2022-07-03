import boto3
import time
client = boto3.client('ec2')
resp1 = client.run_instances(InstanceType='t2.micro',  MaxCount=1, MinCount=1, ImageId='ami-052efd3df9dad4825',
                             TagSpecifications=[
                                 {
                                     'ResourceType': 'instance',
                                     'Tags': [
                                         {
                                             'Key': 'name',
                                             'Value': 'server1'
                                         },
                                     ]
                                 },
                             ])


for x in resp1['Instances']:
    print(x['InstanceId'])
    print(x)

print ("Start : %s" % time.ctime())
time.sleep( 10 )
print ("End : %s" % time.ctime())

resp2 = client.run_instances(InstanceType='t2.micro',  MaxCount=1, MinCount=1, ImageId='ami-052efd3df9dad4825',
                             TagSpecifications=[
                                 {
                                     'ResourceType': 'instance',
                                     'Tags': [
                                         {
                                             'Key': 'name',
                                             'Value': 'server2'
                                         },
                                     ]
                                 },
                             ])


for x in resp2['Instances']:
    print(x['InstanceId'])
    print(x)
    

resp3 = client.describe_instances(Filters=[
        {
            'Name': 'tag:name',            #tag:-----key, values: value (but values is LIST)
            'Values': [
                'server1', 'server2'
            ]
        },


    ])
for x in resp3['Reservations']:
    for y in x['Instances']:
        print('the instance id is {} and instance state  {} & AZ is {} & inst Type is {} & launch time {}'.format(y['InstanceId'],y['State']['Name'],y['Placement']['AvailabilityZone'],y['InstanceType'],y['LaunchTime']))

    
    
    
