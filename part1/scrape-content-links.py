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
    """
    Scrapes content from the provided link and returns a dictionary with relevant information.

    Parameters:
    - link (str): The URL of the webpage to be scraped.

    Returns:
    dict: A dictionary containing the extracted information with the following keys:
        - 'Title': The title of the content.
        - 'Curriculum': The curriculum information.
        - 'Level': The educational level of the content.
        - 'Topics': The topics covered in the content.
        - 'Learning Outcomes Section': The text from the learning outcomes section.
        - 'Introduction': The text from the introduction section.
        - 'Summary Bullets': Comma-separated summary bullets.
        - 'pdf_link': The link to the PDF associated with the content.
    """
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
    """
    Writes the extracted data to a CSV file.

    Parameters:
    - output_data (list): A list of dictionaries, where each dictionary represents the extracted data from a webpage.

    Returns:
    None
    """
    fieldnames = ['Title', 'Curriculum', 'Level', 'Topics', 'Learning Outcomes Section', 'Introduction', 'Summary Bullets', 'pdf_link']
    csv_output_path = './resources/raw_content.csv'
    # Write data to the CSV file
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for data in output_data:
            writer.writerow(data)
def upload_to_s3(path):
    """
    Uploads a file to an Amazon S3 bucket.

    Parameters:
    - path (str): The local path of the file to be uploaded.

    Returns:
    None
    """
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    bucket_name = 'cfainstitute-topic-details-raw'
    s3_key = 'raw_content.csv'  

    df = pd.read_csv(path)

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    csv_data = df.to_csv(index=False)
    s3.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)

def extract_content():
    """
    Extracts content from multiple links specified in a CSV file, writes the extracted data to a local CSV file,
    and uploads it to an Amazon S3 bucket.

    Parameters:
    None

    Returns:
    None
    """
    csv_file_path = './resources/links.csv'
     # Initialize an empty list to store extracted data
    output_data = []
    # Read links from the CSV file and extract data
    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  
        for row in csv_reader:
            link = row[0]  # Assuming the link is in the first column
            data = extract_data(link)
            if data:
                output_data.append(data)
    # Write the extracted data to a local CSV file
    write_to_csv(output_data=output_data)
    # Upload the local CSV file to Amazon S3
    upload_to_s3(path='./resources/raw_content.csv')


#start extracting the content from links 
extract_content()