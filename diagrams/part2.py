from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.programming.language import Python
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.generic.database import SQL

with Diagram("Part2", show=False, direction="TB"):
    pytext = Python("extract_text_pypdf") 
    ecl = Python("extract_text_grobid")  
    xml_to_txt = Python("xml_to_txt")  
    emd_pypdf = Python("extract_metadata")  
    emd_pypdf = Python("extract_metadata")  

    upload_data_to_snowflake = Python("upload_content_to_snowflake")
    upload_data_to_snowflake_pypdf_metadata = Python("upload_data_to_snowflake_pypdf_metadata")
    upload_data_to_snowflake_grobid_metadata = Python("upload_data_to_snowflake_grobid_metadata")
    
    MetadataDB = SQL("MetadataDB")
    LearningOutcomesDB = SQL("LearningOutcomesDB")

    pypdf = SimpleStorageServiceS3Bucket("	cfainstitute-learning-outcomes-raw/pypdf")
    grobid = SimpleStorageServiceS3Bucket("	cfainstitute-learning-outcomes-raw/grobid")

    pytext >> pypdf 
    ecl >> xml_to_txt
    xml_to_txt >> grobid
    
    upload_data_to_snowflake >> LearningOutcomesDB

    
    upload_data_to_snowflake_pypdf_metadata >> MetadataDB
    upload_data_to_snowflake_grobid_metadata >> MetadataDB
    

    