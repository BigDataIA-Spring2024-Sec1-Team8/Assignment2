from grobid_client.grobid_client import GrobidClient
import os

if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")

    client.process("processHeaderDocument", "../resources", output="../resources/metadata", consolidate_citations=True, tei_coordinates=True, force=True, consolidate_header=True)
