from setuptools import setup

setup(
    name='europeana-search',
    version='0.1.0',
    author='Martin Keegan',
    author_email='martin@no.ucant.org',
    packages=['europeana'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Basic Python wrapper for Europeana Search API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests"
    ],
)