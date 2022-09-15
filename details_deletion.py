import boto3
TAGS = ['production', 'development']
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()
tags = {}
for tag in instances:
 tags[tag['Key']] = tag['Value']
 if('Purpose' not in tags or tags['Purpose'] not in TAGS):
   instances.stop()

  
