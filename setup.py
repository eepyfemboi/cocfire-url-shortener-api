from setuptools import setup, find_packages

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name='cocfire-url-shortener-api',
    version='0.0.5',
    long_description = long_description,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
