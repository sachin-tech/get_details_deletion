import boto3
TAGS = ['production', 'development']
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:Purpose', 'Values': ['Production']}])
for instance in instances:
   id=instance.id
   ec2.instances.filter(InstanceIds=[id]).stop()
   print("Instance ID is stopped:- "+instance.id)
   
  

  
