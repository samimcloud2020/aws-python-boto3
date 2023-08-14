import json
from datetime import datetime
import time
from zoneinfo import ZoneInfo
import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    #event = json.loads(event)
    #print(json.dumps(event, indent=4, sort_keys=True))
    account = event["account"]
    time = event["time"]
    region = event["region"]
    type = event["detail"]["type"]
    resourceType = event["detail"]["resource"]["resourceType"]
    instanceId = event["detail"]["resource"]["instanceDetails"]["instanceId"]
    instanceType = event["detail"]["resource"]["instanceDetails"]["instanceType"]
    ipAddressV4 = event["detail"]["service"]['action']['networkConnectionAction']['remoteIpDetails']['ipAddressV4']
    countryName = event["detail"]["service"]['action']['networkConnectionAction']['remoteIpDetails']['country']['countryName']
    print(countryName)
    
    # India Time
    current_datetime = datetime.now(tz=ZoneInfo("Asia/Kolkata"))
    # getting the date and time from the current date and time in the given format
    current_date_time = current_datetime.strftime("%d/%m/%Y, %H:%M:%S")
    print("current date and time = ",current_date_time)
   
    message = {"countryName": countryName}
    response = client.publish(
    TopicArn='arn:aws:sns:us-east-1:291222035571:topic1',    
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json',
    MessageAttributes={
                        'countryName': {
                            'DataType': 'String',
                            'StringValue': countryName
                        }
                    },

                    )
    return response
