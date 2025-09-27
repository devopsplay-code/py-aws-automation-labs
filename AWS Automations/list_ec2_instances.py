import boto3   # 1️⃣ Bring the AWS helper toolbox into Python

# 2️⃣ Call the EC2 service office (client)
ec2 = boto3.client('ec2')

# 3️⃣ Ask EC2 office:
#    "Hey, tell me about every machine I own."
response = ec2.describe_instances()

# 4️⃣ Go through the big answer and pick each machine one by one
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])       # like machine's roll number
        print("State:", instance['State']['Name'])          # ON / OFF
        print("Type:", instance['InstanceType'])            # size of the machine
        print("------")
