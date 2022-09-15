import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
#instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['jenkins_server']}, {'Name': 'instance-state-name', 'Values': ['running']}])
instance_object = ec2.Instance()
tags = {}
for tag in instance_object.tags:
 tags[tag['Key']] = tag['Value']
 if('Purpose' not in tags or tags['Purpose'] not in TAGS):
   instance_object.stop()

  
