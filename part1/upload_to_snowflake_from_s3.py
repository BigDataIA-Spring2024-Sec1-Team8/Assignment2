import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

# Extract Snowflake credentials from environment variables
snowflake_account = os.getenv('snowflake_account')
snowflake_user = os.getenv('snowflake_user')
snowflake_password = os.getenv('snowflake_password')
snowflake_warehouse = os.getenv('snowflake_warehouse')
snowflake_schema = os.getenv('snowflake_schema')
# Connect to Snowflake using the extracted credentials
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    schema=snowflake_schema
)
# Create a cursor to execute SQL queries
cursor = conn.cursor()
# Specify target database and table in Snowflake
target_database = 'CFAInstitute'
target_table = 'TopicDetails_s3'
# Create the target database if it does not exist
create_database_query = f"CREATE DATABASE IF NOT EXISTS {target_database}"
cursor.execute(create_database_query)
# Use the target database
use_database_query = f"USE DATABASE {target_database}"
cursor.execute(use_database_query)
# Set the warehouse to be used
cursor.execute("USE WAREHOUSE TEST")
# Create the target table if it does not exist
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    Title VARCHAR,
    Curriculum VARCHAR,
    Level VARCHAR,
    Topics VARCHAR,
    "Learning Outcomes Section" VARCHAR,
    Introduction VARCHAR,
    "Summary Bullets" VARIANT,
    pdf_link VARCHAR
)
"""

cursor.execute(create_table_query)
# Create a file format for CSV data
cursor.execute("""CREATE OR REPLACE FILE FORMAT mycsvformat
   TYPE = 'CSV'
   FIELD_DELIMITER = '|'
   SKIP_HEADER = 1;""")
# Uncomment the following block if you dont have a storage integration

# cursor.execute("""CREATE OR REPLACE STORAGE INTEGRATION part1
#   TYPE = EXTERNAL_STAGE
#   STORAGE_PROVIDER = 'S3'
#   STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::640055273174:role/s3-read-objects'
#   ENABLED = TRUE
#   STORAGE_ALLOWED_LOCATIONS = ('*')
# """)
# Copy data from an S3 bucket into the Snowflake table
cursor.execute(f"""
COPY INTO {target_table}
FROM 's3://cfainstitute-topic-details-processed/'
STORAGE_INTEGRATION = s3_int2
ON_ERROR = CONTINUE
FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '\"' SKIP_HEADER = 1 PARSE_HEADER = FALSE);
""")
