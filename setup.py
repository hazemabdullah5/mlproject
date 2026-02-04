from setuptools import find_packages, setup
from typing import List
from pathlib import Path


HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    Return the list of requirements from a file located next to this setup.py.
    Uses a path relative to this file so metadata generation works when
    pip runs setup.py from a temporary directory.
    '''
    requirements: List[str] = []
    req_path = Path(__file__).parent / file_path
    if not req_path.exists():
        return requirements

    with req_path.open() as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name = "mlproject",
version="0.0.1",
author="Hazem",
author_email="hazemabdulluh5@gmail.com",
packages=find_packages(),
install_requires =get_requirements("requirements.txt")
)