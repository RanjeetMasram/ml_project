from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME = 'housing-prediction'
VERSION = "0.0.4"
AUTHOR = "Ranjeet Masram"
DESCRIPTION = "This is machine Learning project"
PACKAGES = ['housing']
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return a list which contain name
    of libraries mentioned in requirements.txt

    returns:a list which contain name
    of libraries mentioned in requirements.txt
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), 
    install_requires=get_requirements_list()
)
