import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()
tags = {}
for tag in instance_object.tags:
 tags[tag['Key']] = tag['Value']
 if('Purpose' not in tags or tags['Purpose'] not in TAGS):
   instance_object.stop()

  
