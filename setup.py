from setuptools import setup, find_packages

setup(
    name='analysehackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA first python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/SiyandzaD/analysehackathon',
    author='Siyanda',
    author_email='siyandadlamini7@gmail.com'
)
