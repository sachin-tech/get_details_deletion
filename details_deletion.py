import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['Jenkins_Built_instance']}])
for instance in instances:
  print("stopping instance") 
  instance.stop()
  
