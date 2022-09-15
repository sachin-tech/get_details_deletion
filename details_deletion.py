import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    if instance.tags == None:
        print(instance.id)
        instance.stop()
    else:
        instance.start()
