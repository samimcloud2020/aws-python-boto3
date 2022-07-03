mport boto3
ec2 = boto3.resource('ec2')
for x in ec2.instances.all():
    print('the insid {} & insttype {} & state {} & launchtime {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time))
    
