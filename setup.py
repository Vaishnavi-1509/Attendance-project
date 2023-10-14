from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Speech Recognition tool for MySQL Database Management'
LONG_DESCRIPTION = 'This library is built to convert user voice commands into sql commands by catching keywords spoken by the user using Artificial Intelligence of speech recognition.'

# Setting up
setup(
    name="MySQLvoice",
    version=VERSION,
    author="Vaishnavi Gambhir Rao",
    author_email="vaishnavigrao.15@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    packages=find_packages(),
    install_requires=['SpeechRecognition', 'pyaudio', 'mysql-connector-python' ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python ",
        "License :: OSI Approved :: MIT License"
        "Operating System :: Microsoft :: Windows ",
    ]
)