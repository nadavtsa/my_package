from setuptools import setup

setup(
    name='my_package',
    url='https://github.com/nadavtsa/my_package',
    author='nadav',
    author_email='nadav.tsa@gmail.com',
    packages=['my_package', 'bye'],
    long_description=open('README.md').read()
)

# .Values.elasticsearchUrl