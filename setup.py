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
    author='Team LeBron 23',
    author_email='teamlebron23@gmail.com'
)
