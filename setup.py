from setuptools import setup
import pathlib



with open("README.md", "r") as fh:
    long_desc = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()



# This call to setup() does all the work
setup(
    name="lrjson",
    version="0.0.1",
    description="Convert Lightroom Template file .ltemplate into manipulable JSON file",
    keywords='lightroom json lrtemplate photo filter preset',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/remiflavien1/lrjson",
    author="shadawck",
    author_email="hug211mire@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["lrjson"],
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "lrjson=lrjson.__main__:main",
        ]
    },
)