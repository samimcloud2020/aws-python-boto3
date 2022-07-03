#create snapshot of all volumes in all instances in us-east-1 region and mail sent
import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('sns')
snapshot_ids = []
for x in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a','us-east-1b','us-east-1c','us-east-1d','us-east-1f']
    }
]):
    print('Pls print instance id {}'.format(x))
    for y in x.volumes.all():
        snapshot = y.create_snapshot(Description='snapshot created by boto3')
        print('pls print snapshot id {}'.format(snapshot))
        snapshot_ids.append(snapshot.snapshot_id)    #snapshot_ids attribute under EC2:Volume


print('pls print array of snapshotids {}'.format(snapshot_ids))

client.publish(
    TopicArn='arn:aws:sns:us-east-1:663380234130:boto3',
    Message=str(snapshot_ids),  #array snapshot_ids to string conversion
    Subject='Hello Snapshot created for all instances in us-east-1 region'
)
