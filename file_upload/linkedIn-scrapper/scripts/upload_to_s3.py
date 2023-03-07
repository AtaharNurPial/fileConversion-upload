import boto3
import csv
import json

# s3 = boto3.resource('s3')
# bucket = s3.Bucket('linkedin-scrapper-bucket')
# bucket_name = s3.get_bucket_location(Bucket='{{ MyBucketName }}')['LocationConstraint']
s3 = boto3.client('s3')

bucket_name = "linkedin-scrapper-bucket"
file_path = '../../../file_conversion/data/data.csv'

# response = s3.put_object(
#     Bucket=bucket_name,
#     Key=
# )

with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Convert the CSV data to a list of dictionaries
    data = []
    for row in csv_reader:
        data.append(row)
json_data = json.loads(json.dumps(data))

key = json_data[0].get("Name")

with open(file_path, 'rb') as file:
    s3.upload_fileobj(file, bucket_name, f'{key}.csv')
print(f'upload completed...')

def create_presigned_url(bucket_name, object_name, expiration=600):
    s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',))

    try:
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                            ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return "Error"
    
    return response
signed_url = create_presigned_url(bucket_name=bucket_name,object_name=f"{key}.csv")
print(f"{signed_url = }")


