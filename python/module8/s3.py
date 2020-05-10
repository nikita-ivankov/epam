import boto3

def copy_to_bucket(input_buckets, output_bucket):
    s3 = boto3.client('s3')
    try:
        print(s3.head_bucket(Bucket=output_bucket))
    except:
        print(f'Bucket {output_bucket} is not exist, creating...')
        s3.create_bucket(Bucket=output_bucket)
        print(f'New bucket {output_bucket} has been successfuly created')

    for input_bucket in input_buckets:
        print(f'Moving files from bucket {input_bucket}')
        for key in s3.list_objects(Bucket=input_bucket)['Contents']:
            file_name = key['Key']
            print(f'  file - {file_name}')
            copy_source = {
                'Bucket': input_bucket,
                'Key': file_name
            }
            s3.copy(copy_source, output_bucket, file_name)
            print('  Completed')

if __name__ == "__main__":
    copy_to_bucket(['ivankov2020input',	'ivankov2020output0905'],'ivankov2020output09')

