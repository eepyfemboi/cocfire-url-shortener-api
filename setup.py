from setuptools import setup, find_packages

setup(
    name='cocfire-url-shortener-api',
    version='0.0.1',
    description='The official api wrapper for my URL shortener',
    long_description='The official api wrapper for my URL shortener',
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
