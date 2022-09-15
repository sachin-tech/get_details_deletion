import boto3
TAGS = ['production', 'development']
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:Purpose', 'Values': ['Production']}, {'Name': 'tag:Purpose', 'Values': ['Dev']}])
if instance not in instances:
   instances.stop()

  
