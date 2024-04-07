import os
from pathlib import Path
import logging

## Logging Configuration

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "Text_Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",  ##For doing CICD Deployment using YAML File
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",  ## For all utils related codes
    f"src/{project_name}/utils/common.py",  ## Will write all the utility
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", ## Keep all model related parameters
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"

]

for file_path in list_of_files:
    file_path=Path(file_path) ## Path will make sure all files are in Operating Systems Format like Windows/Linux etc.
    filedir,filename = os.path.split(file_path)

    ##Folder creation
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory {filedir} for the file {filename}")

    ## File creation
    if not(os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating a empty sfile {filename} inside the directory {filedir}")


    else:
        logging.info(f"File {filename} already exists in the directory {filedir}")

