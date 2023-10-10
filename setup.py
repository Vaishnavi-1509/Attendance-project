from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Speech Recognition Attendance for MySQL Database Management'
LONG_DESCRIPTION = 'This library is built to convert user voice commands into sql commands by catching keywords spoken by the user using Artificial Intelligence of speech recognition.'

# Setting up
setup(
    name="MySQLvoice",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('readme.md').read(),
    packages=find_packages(),
    install_requires=['SpeechRecognition', 'pyaudio', 'mysql-connector-python' ],
)
