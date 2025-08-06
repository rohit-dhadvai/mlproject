from setuptools import setup, find_packages
from typing import List
import os
import re

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''

    This function reads a requirements file and returns a list of requirements. 

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

def get_version():
    """
    Reads __version__ from src/__init__.py without importing the package.
    """
    version_file = os.path.join("src", "__init__.py")
    with open(version_file, "r") as f:
        content = f.read()
    match = re.search(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]", content, re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError("Version not found in __init__.py")

setup(
    name='mlproject',
    version=get_version(),
    author='Rohit',
    author_email='rohitdhadvai26@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt')
)