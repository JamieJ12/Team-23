from setuptools import setup, find_packages

setup(
    name='Functions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Functions of Eskom data metrics.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],['pandas'],
    url='https://github.com/JamieJ12/Team-23',
    author='Team LeBron 23(Jamie Japhta, Mpumelelo Ndlovu, Precious Sekgathume, Amukelani Ngobeni, Mbuso Biyela)',
    author_email='teamlebron23@gmail.com'
)
