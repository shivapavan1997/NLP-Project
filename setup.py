from setuptools import setup,find_packages
from typing import List

PROJECT_NAME='NLP PROJECT'
VERSION="1.0.0"
DESCRIPTION='ML Project in modular coding'
AUTHOR='Shiva Pavan'
AUTHOR_EMAIL='shivapavan1060@gmail.com'

REQUIREMENTS_FILE_NAME="requirements.txt"
HYPEN_E_DOT="-e ."


# Requirements.txt file open
#read
#
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as f:
        requirement_list=f.readlines()
        requirement_list= [requirement_name.strip() for requirement_name in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
            return requirement_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )