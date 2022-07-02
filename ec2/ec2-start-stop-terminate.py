import boto3
import time
client = boto3.client('ec2')

resp2 = client.start_instances(InstanceIds=['i-014f56f307de7bb2a'])
for x in resp2['StartingInstances']:
    print(x['InstanceId'])
    print(x)

print ("Start : %s" % time.ctime())
time.sleep( 80 )
print ("End : %s" % time.ctime())

resp3 = client.stop_instances(InstanceIds=['i-014f56f307de7bb2a'])

for x in resp3['StoppingInstances']:
    print(x['InstanceId'])
    print(x)

print ("Start : %s" % time.ctime())
time.sleep( 80 )
print ("End : %s" % time.ctime())

resp4 = client.terminate_instances(InstanceIds=['i-014f56f307de7bb2a'])

for x in resp4['TerminatingInstances']:
    print(x['InstanceId'])
    print(x)
