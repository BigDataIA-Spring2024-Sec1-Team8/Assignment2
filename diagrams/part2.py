from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.programming.language import Python
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.generic.database import SQL


with Diagram("Part2 Grobid", show=False, direction="TB"):
    ecl = Python("extract_text")  
    xml_to_txt = Python("xml_to_txt")  

    extract_metadata_grobid = Python("extract_metadata")  

    upload_data_to_snowflake = Python("upload_content")
    upload_data_to_snowflake_grobid_metadata = Python("upload_metadata")
    
    MetadataDB = SQL("MetadataDB")
    LearningOutcomesDB = SQL("LearningOutcomesDB")

    grobid = SimpleStorageServiceS3Bucket("learning-outcomes grobid")

    ecl >> xml_to_txt
    xml_to_txt >> grobid
    
    upload_data_to_snowflake >> LearningOutcomesDB
    extract_metadata_grobid >> upload_data_to_snowflake_grobid_metadata >> MetadataDB
    
with Diagram("Part2 pypdf", show=False, direction="TB"):
    pytext = Python("extract_text") 

    upload_data_to_snowflake_pypdf_metadata = Python("upload pypdf_metadata")
    
    MetadataDB = SQL("MetadataDB")

    pypdf = SimpleStorageServiceS3Bucket("learning-outcomes pypdf")

    pytext >> pypdf     

    
    upload_data_to_snowflake_pypdf_metadata >> MetadataDB
    

    