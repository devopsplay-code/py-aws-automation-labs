# list_buckets.py
import boto3  # bring boto3 toy box

# Connect to S3 service
s3 = boto3.client("s3")

# Ask AWS: "Give me all my buckets"
response = s3.list_buckets()

# Print a friendly message
print("✅ Your S3 Buckets:")

# Loop through each bucket dictionary and print its name
for bucket in response["Buckets"]:
    print("-", bucket["Name"])
