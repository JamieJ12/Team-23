from setuptools import setup, find_packages

setup(
    name='Functions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/JamieJ12/Team-23',
    author='<Your Name>',
    author_email='<Your Email>'
)
