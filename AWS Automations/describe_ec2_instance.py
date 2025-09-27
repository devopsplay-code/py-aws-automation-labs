import boto3   # 1️⃣ Bring AWS helper toolbox

# 2️⃣ Connect to EC2 office
ec2 = boto3.client('ec2')

# 3️⃣ Put the IDs of the machines you want to check
instance_ids = ['i-0123456789abcdef0']  # can add multiple IDs in list

# 4️⃣ Ask EC2 to give info
response = ec2.describe_instances(InstanceIds=instance_ids)

# 5️⃣ Go through the response and print details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
        print("Type:", instance['InstanceType'])
        print("Public IP:", instance.get('PublicIpAddress', 'No Public IP'))
        print("Private IP:", instance['PrivateIpAddress'])
        print("Launch Time:", instance['LaunchTime'])
        print("Tags:", instance.get('Tags', 'No Tags'))
        print("------")
