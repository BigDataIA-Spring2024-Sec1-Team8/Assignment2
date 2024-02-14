from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time,csv
import boto3
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

def scrape_all_pages_for_links(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.coveo-result-list-container')))
    links_details = []

    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.coveo-result-list-container')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        frames = soup.find_all('div', class_='coveo-result-frame coveoforsitecore-template')
        
        for frame in frames:
            article = frame.find('div', class_='coveo-result-row')
            link_tag = article.find('a', class_='CoveoResultLink')
            result_meta_items = article.find_all('span', class_='result-meta-item')
            subtexts = ' '.join(item.text for item in result_meta_items).strip()
            if link_tag and link_tag['href'] and subtexts:
                text = link_tag.text.strip()
                link = link_tag['href']
                links_details.append({
                    'link': link,
                    'text': text,
                    'subtext': subtexts
                })
        
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.coveo-pager-next')
            if "coveo-disabled" in next_button.get_attribute("class"):
                break  
            else:
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(5)
        except:
            break  

    return links_details

def create_csv(lists):
    with open('./resources/links.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['link', 'text', 'subtext']
        fieldnames = ['link', 'text', 'subtext']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()

        csv_writer.writerows(lists)
def upload_to_s3(path):
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    bucket_name = 'cfainstitute-topic-details-raw'
    s3_key = 'raw_links.csv'  

    df = pd.read_csv(path)

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    csv_data = df.to_csv(index=False)
    s3.put_object(Body=csv_data, Bucket=bucket_name, Key=s3_key)

def scrapeLiks():
    driver = webdriver.Chrome()  
    url = 'https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending&numberOfResults=25'
    article_links_details = scrape_all_pages_for_links(driver, url)
    driver.quit()
    create_csv(article_links_details)
    upload_to_s3('./resources/links.csv')
scrapeLiks()
