import boto3   # 1️⃣ Bring the AWS helper toolbox

# 2️⃣ Connect to EC2 office
ec2 = boto3.client('ec2')

# 3️⃣ Put the ID of the machine you want to delete
instance_id = 'i-0932da3337ea562f4'  # replace with your real ID

# 4️⃣ Tell EC2 to terminate it
response = ec2.terminate_instances(InstanceIds=[instance_id])

print("Terminating instance:", instance_id)
print(response)
