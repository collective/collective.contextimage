from setuptools import setup, find_packages
import os

version = "0.4"

setup(name='collective.contextimage',
      version=version,
      description="",
      long_description="",
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='web zope plone theme',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
      ],
      )
