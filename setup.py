from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pythra",
    version="0.2.1",
    author="johndev4",
    author_email="mail@johndev4.com",
    description="Translate python keywords in any language to English equivalent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johndev4/pythra",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    install_requires=[
        "typer==0.7.0"
    ],
    entry_points={
        "console_scripts": [
            "pythra=src.main:init_app",
        ],
    },
)
