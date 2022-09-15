import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
base = ec2.instances.filter()
filters = [{
    'Key': 'Name',
    'Values': ['Jenkins_Built_instance']
}]
filtered1 = base.filter(Filters=filters)
for instance in filtered1:
  print(instance.id)
