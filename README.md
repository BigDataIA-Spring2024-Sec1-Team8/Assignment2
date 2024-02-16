# Assignment2

## Project Description
The project is structured into two primary components aimed at streamlining the acquisition and organization of educational resources from the CFA Institute. Part 1 is dedicated to the web-scraping of the CFA Institute’s Refresher Readings webpage (https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending) , systematically extracting content to be curated into a structured CSV file. This CSV file is subsequently uploaded to Snowflake with the help of SQLAlchemy, ensuring the data is securely stored and ready for analysis within the cloud-based data warehouse. Part 2 expands the scope of data handling by automating the extraction of text from PDF documents through the use of PyPDF2 and Grobid. The extracted textual data is organized into text files and uploaded to AWS S3 for reliable and centralized storage, while metadata related to the documents is concurrently uploaded to Snowflake. This meticulous approach guarantees an integrated repository where documents are not only stored but also accompanied by their relevant metadata.

## Project Resources
* **Google Codelab link** - https://codelabs-preview.appspot.com/?file_id=1MQWcii-VMXXTCjRpnW2LeLw88TdDjGMXlnuIGz4oHK0#0
* **PyPDF Extraction** - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/blob/main/part2/pypdf_extract.py
* **Grobid Extraction** - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/blob/main/part2/grobid_client_extraction/grobid_metadata_extract.py

## Tech Stack

BeautifulSoup | Selenium | PyPDF2 | Grobid | SQLAlchemy | AWS S3 | Snowflake

## Architecture Diagram

#### Part1 CFA RR Web Scraping

![rZcbL8eVRLrVdOgvSv7OqQpZeUofnE_UHU82mvcWWxnNWohXMFuYZu_wc9bFZ76w-D59TpiJpJZPFPQoKlC_8jYpbLRM083WsucYpLN1STAmd14gqE93HHVpXtT6](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/92ed0859-dd00-4489-84b7-cfb98ddf2f92)

#### Process Flow 
It automates the collection of educational materials from the CFA Institute's website. It scrapes and captures content links, consolidates the data into a CSV, and stores it in the cloud. This structured information is then uploaded to Snowflake using SQLAlchemy, ensuring organized data storage and streamlined access for future analysis within a cloud-based data warehouse.

#### Part 2 PDF Text Extraction
#### Grobid Extraction
![Blank diagram (1)](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/5d5867f6-4abf-4f2f-8f6e-2faf52a66313)

#### Process Flow
A workflow for PDF data extraction and storage, utilizing Grobid for text parsing, Python for XML processing, and Amazon S3 for text storage, with metadata management handled by SQLAlchemy and Snowflake. After Grobid processes the PDFs, scripts convert XML to text, extract metadata, and store both elements—text in S3 and metadata in Snowflake—facilitating efficient data use and analysis.

#### PyPDF Extraction
![Blank diagram (4)](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/1200edb7-00ff-4652-9aeb-9a28b09d6a79)

#### Process Flow
In this process, PDF files are first read by a Python script. This script uses the PyPDF2 library, a tool for extracting text and metadata from PDF files. The extracted text is then stored in Amazon S3 which ensures that the raw text data is kept in a secure and accessible place.
In parallel, metadata extracted from the PDFs, which may include information like author, title, and publication date, is uploaded to Snowflake using SQLAlchemy. SQLAlchemy is a Python SQL toolkit and Object-Relational Mapping (ORM) library that facilitates database interactions. 

## Repository Structure

<img width="316" alt="Screenshot 2024-02-16 at 12 13 47 PM" src="https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment2/assets/114782541/98f51e8f-fca7-444a-b170-56bf196a6600">

## Contributions 
* Sai Durga Mahesh Bandaru - 33.3%
* Sri Poojitha Mandali - 33.3%
* Shivani Gulgani - 33.3%

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

