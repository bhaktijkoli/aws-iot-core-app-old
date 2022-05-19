# import os
# import boto3
# from dotenv import load_dotenv
# load_dotenv()

# aws_region = os.getenv("AWS_REGION")
# aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
# aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
# aws_thing_name = os.getenv("AWS_THING_NAME")
# aws_thing_type_name = os.getenv("AWS_THING_TYPE_NAME")

# client = boto3.client("iot",
#                       region_name=aws_region,
#                       aws_access_key_id=aws_access_key_id,
#                       aws_secret_access_key=aws_secret_access_key
#                       )

# response = client.create_thing(
#     thingName=aws_thing_name,
#     thingTypeName=aws_thing_type_name,
# )

# print(response)
print("Hello from iot App")
