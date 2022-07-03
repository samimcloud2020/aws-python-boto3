import boto3
ec2 = boto3.resource('ec2')
ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a','us-east-1b','us-east-1c','us-east-1d','us-east-1f']
    }
]).start()
ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a','us-east-1b','us-east-1c','us-east-1d','us-east-1f']
    }
]).stop()
ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a','us-east-1b','us-east-1c','us-east-1d','us-east-1f']
    }
]).terminate()
