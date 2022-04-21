"""
********************************************************************
* Author = https://github.com/alexbonella                          *                       
* Date = '12/03/2022'                                              *
* Description = Stats Channel DE Latam                             *                      
********************************************************************
"""


import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import credentials
import numpy as np
import argparse
import random
import time
from datetime import datetime
import datetime
from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2
import os
import shutil
import boto3



# Get permission
DEVELOPER_KEY = credentials.DEVELOPER_KEY
CHANNEL_ID = credentials.channel_id

# Local_Directory
os.chdir('/home/ubuntu/de_latam_scripts')



# Url Channel Stats
url_channel_stats = 'https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id='+CHANNEL_ID+'&key='+DEVELOPER_KEY
response_channels = requests.get(url_channel_stats)
aws_channel_stat = json.loads(response_channels.content)
channel_stats = aws_channel_stat['items'][0]['statistics']
hora = datetime.datetime.now()
date = hora.strftime("%Y-%m-%d")

# Create Dict
data_channel = {

            'Date':date,
            'Total_Views':int(float(channel_stats['viewCount'])),
            'Subscribers':int(float(channel_stats['subscriberCount'])),
            'Video_count':int(float(channel_stats['videoCount']))
                        }

with open('stats_channel_'+date.split()[0].replace('-','_')+'.json', "w") as outfile:
        json.dump(data_channel, outfile)
        outfile.close()


# Send File To S3
s3 = boto3.resource("s3")
BUCKET = "--------" # Bucket Name

# Upload file to S3
s3.Bucket(BUCKET).upload_file('stats_channel_'+date.split()[0].replace('-','_')+'.json','stats_channel_'+date.split()[0].replace('-','_')+'.json')

# Remove File
os.remove('stats_channel_'+date.split()[0].replace('-','_')+'.json')

print('/n')
print('END')