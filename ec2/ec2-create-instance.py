import boto3
client = boto3.client('ec2')
response = client.run_instances(InstanceType='t2.micro',  MaxCount=3, MinCount=2, ImageId='ami-052efd3df9dad4825' )
for x in response['Instances']:
    print(x['InstanceId'])
    print(x)
