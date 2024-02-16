import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv
load_dotenv()

snowflake_account = os.getenv('snowflake_account')
snowflake_user = os.getenv('snowflake_user')
snowflake_password = os.getenv('snowflake_password')
snowflake_warehouse = os.getenv('snowflake_warehouse')
snowflake_schema = os.getenv('snowflake_schema')

conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    schema=snowflake_schema
)

cursor = conn.cursor()

target_database = 'CFAInstitute'
target_table = 'TopicDetails_s3'

create_database_query = f"CREATE DATABASE IF NOT EXISTS {target_database}"
cursor.execute(create_database_query)

use_database_query = f"USE DATABASE {target_database}"
cursor.execute(use_database_query)
cursor.execute("USE WAREHOUSE TEST")

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

cursor.execute("""CREATE OR REPLACE FILE FORMAT mycsvformat
   TYPE = 'CSV'
   FIELD_DELIMITER = '|'
   SKIP_HEADER = 1;""")

# cursor.execute("""CREATE OR REPLACE STORAGE INTEGRATION part1
#   TYPE = EXTERNAL_STAGE
#   STORAGE_PROVIDER = 'S3'
#   STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::640055273174:role/s3-read-objects'
#   ENABLED = TRUE
#   STORAGE_ALLOWED_LOCATIONS = ('*')
# """)

cursor.execute(f"""
COPY INTO {target_table}
FROM 's3://cfainstitute-topic-details-processed/'
STORAGE_INTEGRATION = s3_int2
ON_ERROR = CONTINUE
FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '\"' SKIP_HEADER = 1 PARSE_HEADER = FALSE);
""")
