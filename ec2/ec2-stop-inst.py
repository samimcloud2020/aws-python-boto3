import boto3
client = boto3.client('ec2')
resp2 = client.stop_instances(InstanceIds=['i-014f56f307de7bb2a'])

for x in resp2['StoppingInstances']:
    print(x['InstanceId'])
    print(x)
