import boto3, json
import os
from model_utils import GetObjectModel
from aws_lambda_powertools.utilities.parser import parse

bucket_name = os.environ.get('S3BUCKETNAME')
s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',))

def lambda_handler(event, context):
    try:
        parsed_body: GetObjectModel = parse(event=event["body"], model=GetObjectModel)

        response_dict = parsed_body.dict()
        print(f"{response_dict = }")
        obj_name = response_dict.get('key')

        response = create_presigned_url(bucket_name=bucket_name,object_name=f"{obj_name}.csv")
        print(f"{response = }")

        return {
            "statusCode": 200,
            "body": json.dumps(
            {
            "message": "signed url obtained successfully!",
            "signed_url": response
            }
            )
        }
    except Exception as e:
        print(e)
        return{
            "statusCode": 400,
            "message": str(e)
        }

def create_presigned_url(bucket_name, object_name, expiration=600):

    # boto3.setup_default_session(profile_name='shadhin')

    try:
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return "Error"

    # The response contains the presigned URL
    # print(response)
#     curl_url = f"""curl -X PUT -T '{ec2_src_prefix}{file_name}' '{response}' \
# --header 'Content-Type: application/zip'"""
#     print(curl_url)
    return response