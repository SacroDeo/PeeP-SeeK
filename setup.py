from setuptools import setup, find_packages

setup(
    name="allfinder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "holehe",
        "sherlock",
        "beautifulsoup4",
        "pandas",
        "python-whois",
    ],
)
