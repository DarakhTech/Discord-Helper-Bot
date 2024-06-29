from setuptools import find_packages, setup
from typing import List

EDOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """This function returns a list of requirements"""
    
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if EDOT in requirements:
            requirements.remove(EDOT)

setup(
name = "DiscordBot",
version = "0.0.1",
author = "Darakh",
author_email = "darakhtech@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)