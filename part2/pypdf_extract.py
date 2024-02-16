import PyPDF2
import os
import boto3

from dotenv import load_dotenv
load_dotenv()

#Extracting the text from the provided PDFs
def extract_text_from_pdf(pdf_path):
    text = ''
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        #Extracting text from all pages
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
            
    return text

#Writing the extracted text to a txt file
def save_text_to_txtfile(pdf_path, text):
    # Extract the PDF name without the extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_filename = f"./resources/pypdf/PyPDF_RR_2024_{pdf_name}.txt"
    with open(txt_filename, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

#Paths which lead to the PDFs from which text is to be extracted
pdf_paths = ['./resources/Level1_combined.pdf', './resources/Level2_combined.pdf', './resources/Level3_combined.pdf']

#Initiating a loop for getting every path 
for pdf_path in pdf_paths:
    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_txtfile(pdf_path, extracted_text)

#Uploading the txt file to S3 from local
def upload_folder_to_s3(local_folder_path, s3_bucket_name, s3_folder_path, aws_access_key_id, aws_secret_access_key):
    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Iterate through all the files in the local folder
    for root, dirs, files in os.walk(local_folder_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_file_path, local_folder_path)
            s3_object_key = os.path.join(s3_folder_path, s3_key).replace("\\", "/")  # Replace backslashes with forward slashes for cross-platform compatibility

            # Upload each file to S3
            print(f"Uploading {local_file_path} to s3://{s3_bucket_name}/{s3_object_key}")
            s3.upload_file(local_file_path, s3_bucket_name, s3_object_key)

local_folder_path = './resources/pypdf'
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
bucket_name = 'cfainstitute-learning-outcomes-raw'
s3_folder_path = 'pypdf'
upload_folder_to_s3(local_folder_path, bucket_name, s3_folder_path, aws_access_key_id, aws_secret_access_key,)
