from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='Breast Lesion',
      version="0.0.1",
      description="Breast_lesion (API ready)",
      license="MIT",
      author="KTLeWagon",
      author_email="contact@lewagon.org",
      #url="https://github.com/KTLeWagon/breast_lesion_DL",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
