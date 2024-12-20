#!/usr/bin/env python3
import json
import os

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3 import S3ServiceResource

PRI_BUCKET_NAME = 'vincent-sample'
PRI_BUCKET_NAME2 = 'vincent-sample2'
ENDPOINT_URL = "http://localhost:4566"
F1 = "lil1.txt"
F2 = "lil2.txt"
F3 = "lil3.txt"
DIR = "./"
DOWN_DIR = "./"
REGION = 'eu-west-1'

def upload_file(bucket, directory, file, s3, s3path=None):
    file_path = directory + '/' + file
    remote_path = s3path
    if remote_path is None:
        remote_path = file
    try:
        s3.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)

def list_objects(bucket, s3):
    try:
        response = s3.meta.client.list_objects(Bucket=bucket)
        objects = []

        if 'Contents' not in response:
            print('No object inside')
            return objects

        for content in response['Contents']:
            file_name = content['Key']
            print(file_name)
            objects.append(file_name)
        print(bucket, 'contains', len(objects), 'files')
        return objects
    except ClientError as ce:
        print('error', ce)

def generate_download_link(bucket, key, expiration_seconds, s3):
    try:
        response = s3.meta.client.generate_presigned_url('get_object', Params={
            'Bucket': bucket,
            'Key': key
        }, ExpiresIn=expiration_seconds)
        print(response)
    except ClientError as ce:
        print('error', ce)

def copy_file(source_bucket, destination_bucket, source_key, destination_key, s3):
    try:
        source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        s3.Bucket(destination_bucket).copy(source, destination_key)
    except ClientError as ce:
        print('error', ce)

def download_file(bucket, directory, local_name, key_name, s3):
    file_path = directory + '/' + local_name + '.downloaded'
    try:
        s3.Bucket(bucket).download_file(key_name, file_path)
    except ClientError as ce:
        print('error', ce)

def delete_local_files(directory, local_name):
    file_path = directory + '/' + local_name + '.downloaded'
    os.remove(file_path)

def delete_files(bucket, keys, s3):
    objects = []
    for key in keys:
        objects.append({'Key': key})
    try:
        s3.Bucket(bucket).delete_objects(Delete={'Objects': objects})
    except ClientError as ce:
        print('error', ce)

def delete_bucket(name, s3):
    try:
        bucket = s3.Bucket(name)
        bucket.objects.all().delete()
        bucket.delete()
    except ClientError as ce:
        print('error', ce)

def apply_bucket_policy(bucket, s3, policy_file):
    try:
        with open(policy_file, 'r') as file:
            policy = json.load(file)
        s3.meta.client.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
    except ClientError as ce:
        print(f"Error applying bucket policy to {bucket}: {ce}")

def prevent_public_access(bucket, s3):
    try:
        s3.meta.client.put_public_access_block(Bucket=bucket,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            })
        apply_bucket_policy(bucket, s3, './policies/p2.json')
    except ClientError as ce:
        print('error', ce)

def create_bucket(name, s3):
    try:
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={
                'LocationConstraint': REGION
            }
        )
    except ClientError as ce:
        print('error', ce)

def main():
    """entry point"""
    s3: S3ServiceResource = boto3.resource('s3', endpoint_url=ENDPOINT_URL)

    # create bucket
    create_bucket(PRI_BUCKET_NAME, s3)
    create_bucket(PRI_BUCKET_NAME2, s3)

    # Upload files to bucket
    upload_file(PRI_BUCKET_NAME, DIR, F1, s3)
    upload_file(PRI_BUCKET_NAME, DIR, F2, s3)
    upload_file(PRI_BUCKET_NAME, DIR, F3, s3)

    generate_download_link(PRI_BUCKET_NAME, F3, 5, s3)

    # download file
    download_file(PRI_BUCKET_NAME, DOWN_DIR, F3, F3, s3)

    # delete downloaded file
    delete_local_files(DOWN_DIR, F3)

    # list files in bucket
    list_objects(PRI_BUCKET_NAME, s3)

    # copy files in bucket
    copy_file(PRI_BUCKET_NAME, PRI_BUCKET_NAME2, F1, F2, s3)

    # delete files in bucket
    delete_files(PRI_BUCKET_NAME, [F1, F2, F3], s3)

    prevent_public_access(PRI_BUCKET_NAME, s3)

    # delete buckets
    delete_bucket(PRI_BUCKET_NAME, s3)
    delete_bucket(PRI_BUCKET_NAME2, s3)

if __name__ == '__main__':
    main()
