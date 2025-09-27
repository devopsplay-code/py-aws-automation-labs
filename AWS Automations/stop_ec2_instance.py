import boto3   # 1️⃣ Bring the AWS helper toolbox

# 2️⃣ Connect to EC2 office
ec2 = boto3.client('ec2')

# 3️⃣ Put the ID of the machine you want to stop
# 👉 Replace with your real Instance ID
instance_id = 'i-0932da3337ea562f4'

# 4️⃣ Tell EC2 to stop it
response = ec2.stop_instances(InstanceIds=[instance_id])

print("Stopping instance:", instance_id)
print(response)
