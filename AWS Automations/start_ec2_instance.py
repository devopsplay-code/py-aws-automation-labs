import boto3   # 1️⃣ Bring the AWS helper toolbox

# 2️⃣ Connect to EC2 office
ec2 = boto3.client('ec2')

# 3️⃣ Put the ID of the machine you want to start
# 👉 Replace with your real Instance ID (example below)
instance_id = 'i-0932da3337ea562f4'

# 4️⃣ Tell EC2 to start it
response = ec2.start_instances(InstanceIds=[instance_id])

print("Starting instance:", instance_id)
print(response)
