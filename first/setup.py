from setuptools import setup

setup(
    name='my_package',
    url='https://github.com/nadavtsa/my_package.git',
    author='nadav',
    author_email='nadav.tsa@gmail.com',
    packages=['hello'],
    long_description=open('README.txt').read()
)