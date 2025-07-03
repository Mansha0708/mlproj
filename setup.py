from setuptools import find_packages , setup
from typing import List

hed="-e ."
def get_requirements(file_path:str)->List[str]:
    # this function reyturn list of req
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if hed in requirements:
            requirements.remove(hed)
    return requirements
setup(
    name="mlproj",
    version="0.0.1",
    author="mansha",
    author_email="manshaahuja0708@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)