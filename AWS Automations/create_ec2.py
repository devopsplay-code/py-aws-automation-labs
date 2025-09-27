import boto3
from botocore.exceptions import ClientError

# Step 1: Connect to EC2 service
ec2 = boto3.resource('ec2')

try:
    # Step 2: Launch 2 EC2 instances
    instances = ec2.create_instances(
        ImageId='ami-046c2381f11878233',   # Amazon Linux 2 (ap-south-1)
        MinCount=1,
        MaxCount=2,                        # Launch 2 instances
        InstanceType='t2.micro',           # Free tier
        KeyName='ec2-key',                 # Replace with YOUR key pair name
        SecurityGroups=['default-ec2'],    # Replace with your SG
        TagSpecifications=[                # Step 3: Add Name tag
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'MyFirstEC2'}
                ]
            }
        ]
    )

    # Step 4: Print all instance IDs
    for instance in instances:
        print("✅ EC2 Instance Launched 🚀 With ID:", instance.id)

except ClientError as e:
    print("❌ Something went wrong:", e)
