import boto3
# connect to EC2 service
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
    ImageId='ami-046c2381f11878233',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='ec2',
    SecurityGroups=['default-ec2']
)

print("EC2 INSTANCE LAUNCHED 🚀 With ID:", instances[0].id)