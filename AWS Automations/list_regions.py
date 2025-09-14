# Step 0: Bring boto3 so Python can talk to AWS
import boto3

# Step 1: Make a "phone" to call the EC2 service
# EC2 is the AWS service that knows all the regions
ec2 = boto3.client("ec2")

# Step 2: Ask AWS: "Which regions do you have?"
response = ec2.describe_regions()

# Step 3: Print a friendly message
print("✅ boto3 is working! Here are some AWS regions:")

# Step 4: Loop through each region dictionary in the list
for region in response["Regions"]:
    # Step 5: Pick the region name and print it
    print("-", region["RegionName"])
