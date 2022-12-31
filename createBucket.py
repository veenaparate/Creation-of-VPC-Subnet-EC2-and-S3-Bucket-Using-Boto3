import boto3
s3_client=boto3.client('s3')
resp=s3_client.create_bucket(
    Bucket='21nov2022bucket'
)