import boto3
ec2 = boto3.resource('ec2')
for x in ec2.instances.all():
    print('All insid {} & insttype {} & state {} & launchtime {} & state {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time,x.state['Name']))



for x in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a','us-east-1b','us-east-1c','us-east-1d','us-east-1f']
    }
]):
    print('Filter insid {} & insttype {} & state {} & launchtime {} & state {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time,x.state['Name']))
