mport boto3
ec2 = boto3.resource('ec2')
for x in ec2.instances.all():
    print('the insid {} & insttype {} & state {} & launchtime {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time))
    
    
import boto3
ec2 = boto3.resource('ec2')
for x in ec2.instances.all():
    print('the insid {} & insttype {} & state {} & launchtime {} & state {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time,x.state['Name']))
    
C:\Users\user\PycharmProjects\aws\venv\Scripts\python.exe C:/Users/user/PycharmProjects/aws/ec2-resource.py
the insid i-0ed631d326c0027d0 & insttype t2.micro & state {'Code': 16, 'Name': 'running'} & launchtime 2022-07-03 08:42:29+00:00 & state running

Process finished with exit code 0    

import boto3
ec2 = boto3.resource('ec2')
for x in ec2.instances.all():
    print('the insid {} & insttype {} & state {} & launchtime {} & state {}'.format(x.instance_id,x.instance_type,x.state,x.launch_time,x.state))
    
    
C:\Users\user\PycharmProjects\aws\venv\Scripts\python.exe C:/Users/user/PycharmProjects/aws/ec2-resource.py
the insid i-0ed631d326c0027d0 & insttype t2.micro & state {'Code': 16, 'Name': 'running'} & launchtime 2022-07-03 08:42:29+00:00 & state {'Code': 16, 'Name': 'running'}

Process finished with exit code 0
