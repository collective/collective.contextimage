from setuptools import setup, find_packages
import os

version = "1.0"
shortdesc = ('Context sensitive images from extended plone content as viewlet, '
             'header, logo, ...')
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()

setup(name='collective.contextimage',
      version=version,
      description="",
      long_description="",
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
            "Framework :: Plone",
            "Framework :: Plone 4.1",
            "Framework :: Plone 4.2",
      ],
      keywords='web zope plone theme viewlet logo header',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'plone.app.layout',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
