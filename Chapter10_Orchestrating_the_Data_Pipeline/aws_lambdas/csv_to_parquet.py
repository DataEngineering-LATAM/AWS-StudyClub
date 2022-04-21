import json
import pandas as pd
from csv import reader
import boto3
import os
import shutil

def lambda_handler(event, context):
    

    
    #metadata
    bucket_name = event['file_info']['bucket_name']
    filename = event['file_info']['filename']
    bucket_destiny = 'gold-paquet-files'
        
        
    s3_client = boto3.client('s3')
    resp = s3_client.get_object(Bucket=bucket_name, Key=filename)
    
    # Create Dataframe
    df = pd.read_csv(resp['Body'], sep=',')
    
    # Crerat Parquet File 
    df.to_parquet('/tmp/'+filename.split('.')[0]+'.parquet') 

    
    # Send File To S3 
    s3 = boto3.resource("s3")
    
    s3.Bucket(bucket_destiny).upload_file('/tmp/'+filename.split('.')[0]+'.parquet', Key=filename.split('.')[0]+'.parquet')
    os.remove('/tmp/'+filename.split('.')[0]+'.parquet')

    
    return filename.split('.')[0]+'.parquet'