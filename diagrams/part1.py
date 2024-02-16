from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.programming.language import Python
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.generic.database import SQL


with Diagram("Part1", show=False, direction="TB"):
    extract_links = Python("extract_links") 
    extract_content_from_links = Python("extract_content_from_links")  
    upload_data_to_snowflake = Python("upload_data_to_snowflake")
    cfainstitute_Raw = SimpleStorageServiceS3Bucket("cfainstitute-topic-details-raw")
    cfainstitute_proc = SimpleStorageServiceS3Bucket("cfainstitute-topic-details-processed")
    DB = SQL("TopicDetailsDB")

    extract_links >> cfainstitute_Raw 
    cfainstitute_Raw >> extract_content_from_links
    extract_content_from_links >> cfainstitute_proc
    cfainstitute_proc >> upload_data_to_snowflake >> DB