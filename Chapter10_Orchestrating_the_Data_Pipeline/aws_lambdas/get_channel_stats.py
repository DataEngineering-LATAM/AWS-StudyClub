import json
import boto3
import pandas as pd


def lambda_handler(event, context):
    
    
    
    # Metadata file 
    bucket_name = event['file_info']['bucket_name']
    filename = event['file_info']['filename']
    fecha = filename.split('stats_channel_')[1].split('.json')[0]
    
    
    # Get Json file
    s3 = boto3.resource('s3')
    content_object = s3.Object(bucket_name, filename)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    
    message = 'Hola Admin !  Las estadisticas del canal para el ' + fecha.replace('_','-') + ' son : n\n\n Total_Views 👉' + str(json_content['Total_Views']) +'\n Subscribers 👉 ' + str(json_content['Subscribers']) +'\n Total_videos 👉 '  +str(json_content['Video_count'])   
    
    return message