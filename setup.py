from setuptools import find_packages, setup
from typing import List

hypen_e_dot = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Fixed replace() issue

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)  # Ensure -e . is removed
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="lakshay",
    author_email="lakshaysh19@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # Fixed typo
)
