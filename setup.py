from setuptools import find_packages, setup


def get_requirements(file_path):
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="Student-Performance-Indicator",
    version="0.0.1",
    author="MSA",
    author_email="mohamed.salaheldin.emam@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)