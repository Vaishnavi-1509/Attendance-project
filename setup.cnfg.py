from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_medium',
    version='0.6',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='vaishnavigambhir15@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Vaishnavi-1509/Attendance-project/edit/main/setup.py',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)