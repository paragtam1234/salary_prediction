from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirement=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
    name='salary_prediction',
    version='0.0.1',
    author='parag',
    author_email='paragtamgadge77@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)