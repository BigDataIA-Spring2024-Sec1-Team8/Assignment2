from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time,csv
import boto3
import pandas as pd
import os
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()


def remove_extra_whitespaces(value):
    if isinstance(value, str):
        return ' '.join(value.split())
    else:
        return value

def preprocess_text(value):
    if isinstance(value, str) and not value.startswith('"'):
        return f'"{value}"'
    else:
        return value

def upload_to_s3(df):
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    bucket_name = 'cfainstitute-topic-details-processed'
    s3_key = 'processed.csv'
    csv_data = df.to_csv(index=False)
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)

def read_and_process():
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    bucket = 'cfainstitute-topic-details-raw'
    key='raw_content.csv'
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(BytesIO(obj['Body'].read()))
    df = df.map(remove_extra_whitespaces)
    df = df.map(preprocess_text)
    df.to_csv('./resources/processed_content.csv', index=False)
    upload_to_s3(df)

read_and_process()