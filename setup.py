from setuptools import setup

setup(name='datapeek',
      version='0.1',
      description='A simple library for dealing with raw data.',
      url='https://github.com/sean-mcclure/datapeek_py',
      author='Sean McClure',
      author_email='sean.mcclure@example.com',
      license='MIT',
      packages=['datapeek'],
      install_requires=[
          'fuzzywuzzy',
          'pandas'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)