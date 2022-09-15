import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['jenkins_server']}, {'Name': 'instance-state-name', 'Values': ['running']}])
instances_to_delete = [to_del for to_del in instances if to_del.id not in [i.id for i in instances]]  
print("stopping instance") 
instance.stop()
  
