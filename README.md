# Assignment2

## Project Description
The project is structured into two primary components aimed at streamlining the acquisition and organization of educational resources from the CFA Institute. Part 1 is dedicated to the web-scraping of the CFA Institute’s Refresher Readings webpage (https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending) , systematically extracting content to be curated into a structured CSV file. This CSV file is subsequently uploaded to Snowflake with the help of SQLAlchemy, ensuring the data is securely stored and ready for analysis within the cloud-based data warehouse. Part 2 expands the scope of data handling by automating the extraction of text from PDF documents through the use of PyPDF2 and Grobid. The extracted textual data is organized into text files and uploaded to AWS S3 for reliable and centralized storage, while metadata related to the documents is concurrently uploaded to Snowflake. This meticulous approach guarantees an integrated repository where documents are not only stored but also accompanied by their relevant metadata.

## Project Resources
* **Google Codelab** - https://codelabs-preview.appspot.com/?file_id=1MQWcii-VMXXTCjRpnW2LeLw88TdDjGMXlnuIGz4oHK0#0
* **Webscrapping & Snowflake** - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/tree/main/part1
* **PyPDF Extraction** - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/blob/main/part2/pypdf_extract.py
* **Grobid Extraction** - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/blob/main/part2/grobid_client_extraction/pdf_to_xml.py

Demonstrations
* **Snowflake upload Demo** - https://northeastern.zoom.us/rec/share/McrcQcNnnkMRREplYTBP_N7orIqrbpHLUJo992smep6xoigZLjhwaHxh9bz8LKsY.sYRV2voDwEmgGFdb 
**Passcode:** 0A.L+U4r
* **Part 1 - Upload with SQLAlchemy** - https://drive.google.com/file/d/1e7lzMEd_M_mmkRUgolD133cbLtUBdCYa/view?usp=sharing
* **Snowflake Upload via script from S3** -https://drive.google.com/file/d/1FKmv6gXNUxEemZZECmQk1HChaglk430q/view?usp=sharing
* **Snowflake Upload via script from local** -https://drive.google.com/file/d/1FKmv6gXNUxEemZZECmQk1HChaglk430q/view?usp=sharing
  
Google Colab
* **Upload XML Content to Snowflake** - https://colab.research.google.com/drive/1a4qn8Ew240i_gOImJFivx6x5T2mHxP-C?usp=sharing
* **Upload Metadata from Grobid** - https://colab.research.google.com/drive/1UXvYaMyr-yiYR0iOFa8NgIjAyo4s8CF_?usp=sharing
* **Upload Metadata from Pypdf** - https://colab.research.google.com/drive/1NTzrSG_Q_WyV9Gi4e2WOtlLJcCkarQkZ?usp=sharing
* **XML Content to Snowflake** - https://colab.research.google.com/drive/1sCdXfklf1s6b0bfdW0l_D4J_6uO3mkwj?usp=sharing
* **XML to TXT** - https://colab.research.google.com/drive/1_K9cMqhK9-L5QYc5xCbEW5pL5TvO0Z9q?usp=sharing



## Tech Stack

BeautifulSoup | Selenium | PyPDF2 | Grobid | SQLAlchemy | AWS S3 | Snowflake

## Architecture Diagram

#### Part1 CFA RR Web Scraping

![rZcbL8eVRLrVdOgvSv7OqQpZeUofnE_UHU82mvcWWxnNWohXMFuYZu_wc9bFZ76w-D59TpiJpJZPFPQoKlC_8jYpbLRM083WsucYpLN1STAmd14gqE93HHVpXtT6](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/92ed0859-dd00-4489-84b7-cfb98ddf2f92)

#### Process Flow 
It automates the collection of educational materials from the CFA Institute's website. It scrapes and captures content links, consolidates the data into a CSV, and stores it in the cloud. This structured information is then uploaded to Snowflake using SQLAlchemy, ensuring organized data storage and streamlined access for future analysis within a cloud-based data warehouse.

#### Part 2 PDF Text Extraction
#### Grobid Extraction
 ![image](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/54bec312-2e1d-4219-91ec-61757a7da14e)

#### Process Flow
A workflow for PDF data extraction and storage, utilizing Grobid for text parsing, Python for XML processing, and Amazon S3 for text storage, with metadata management handled by SQLAlchemy and Snowflake. After Grobid processes the PDFs, scripts convert XML to text, extract metadata, and store both elements—text in S3 and metadata in Snowflake—facilitating efficient data use and analysis.

#### PyPDF Extraction
![Blank diagram (4)](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/1200edb7-00ff-4652-9aeb-9a28b09d6a79)

#### Process Flow
In this process, PDF files are first read by a Python script. This script uses the PyPDF2 library, a tool for extracting text and metadata from PDF files. The extracted text is then stored in Amazon S3 which ensures that the raw text data is kept in a secure and accessible place.
In parallel, metadata extracted from the PDFs, which may include information like author, title, and publication date, is uploaded to Snowflake using SQLAlchemy. SQLAlchemy is a Python SQL toolkit and Object-Relational Mapping (ORM) library that facilitates database interactions. 

## Repository Structure

![Pasted Graphic 1](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/3bb1326f-514a-4519-bdee-0d5d149ac013)

## Contributions 
* Sai Durga Mahesh Bandaru - 33.3%
* Sri Poojitha Mandali - 33.3%
* Shivani Gulgani - 33.3%

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

