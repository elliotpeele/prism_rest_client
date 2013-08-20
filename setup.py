import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    ]

setup(name='prism_rest_client',
      version='0.0',
      description='prism_rest_client',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Elliot Peele',
      author_email='elliot@bentlogic.net',
      url='',
      keywords='web rest client',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='prism_rest_client',
      install_requires=requires,
      )
