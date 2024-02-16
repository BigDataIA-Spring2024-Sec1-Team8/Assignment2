from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time,csv
import boto3
import pandas as pd
import os, requests
from dotenv import load_dotenv
load_dotenv()

def extract_data(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting data using BeautifulSoup
        title = soup.find(class_='article-title').text.strip() if soup.find(class_='article-title') else ''
        curriculum = soup.find(class_='content-utility-curriculum').text.strip() if soup.find(class_='content-utility-curriculum') else ''
        level = soup.find(class_='content-utility-level').text.strip() if soup.find(class_='content-utility-level') else ''
        topics = soup.find(class_='content-utility-topics').text.strip() if soup.find(class_='content-utility-topics') else ''

        # Extracting data after the "Learning Outcomes" section
        learning_outcomes_section = soup.find('h2', text='Learning Outcomes')
        if not (learning_outcomes_section == None):
            section_text = learning_outcomes_section.find_next('section').text.strip()
        else:
            section_text = ""

        introduction_section = soup.find('h2', text='Introduction') or soup.find('h2', string='Overview')
        if not (introduction_section == None):
            introduction_section_text = introduction_section.find_next('section').text.strip()
        else:
            introduction_section_text = ""
        summary_section = soup.find('h2', text='Summary')
        summary_bullets = []
        if not(summary_section==None):
            ul = summary_section.find_next('ul')
            if ul:
                summary_bullets = [li.text.strip() for li in ul.find_all('li')]
        pdf_link=""
        a = soup.find('a', string='Download the full reading (PDF)') 
        if a:
            pdf_link = a['href']
        return {
            'Title': title,
            'Curriculum': curriculum,
            'Level': level,
            'Topics': topics,
            'Learning Outcomes Section': section_text,
            'Introduction': introduction_section_text,
            'Summary Bullets': ', '.join(summary_bullets),
            "pdf_link": pdf_link
        }
    else:
        print(f"Failed to fetch data from {link}")
        return None



def write_to_csv(output_data):
    fieldnames = ['Title', 'Curriculum', 'Level', 'Topics', 'Learning Outcomes Section', 'Introduction', 'Summary Bullets', 'pdf_link']
    csv_output_path = './resources/raw_content.csv'
    # Write data to the CSV file
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for data in output_data:
            writer.writerow(data)
def upload_to_s3(path):
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    bucket_name = 'cfainstitute-topic-details-raw'
    s3_key = 'raw_content.csv'  

    df = pd.read_csv(path)

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    csv_data = df.to_csv(index=False)
    s3.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)

def extract_content():
    csv_file_path = './resources/links.csv' 
    output_data = []

    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  
        for row in csv_reader:
            link = row[0]  
            data = extract_data(link)
            if data:
                output_data.append(data)
    
    write_to_csv(output_data=output_data)
    upload_to_s3(path='./resources/raw_content.csv')

extract_content()