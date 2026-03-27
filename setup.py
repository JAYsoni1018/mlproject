from setuptools import find_packages, setup


def get_requirement(file_path):
    with open(file_path) as f:
        requirement = f.readlines()
    requirement = [req.replace("\n", "") for req in requirement]
    if "-e ." in requirement:
        requirement.remove("-e .")
    return requirement


setup(
    name="mlproject",
    version="0.0.1",
    author="Jay",
    author_email="jaysoni6774@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')

)
