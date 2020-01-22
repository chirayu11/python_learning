from setuptools import setup, find_packages

setup(name='python_learning',
      version='0.1',
      description='Different algorithms and data structures implemented in Python',
      packages=find_packages(),
      url='https://github.com/chirayu11/python_learning',
      install_requires=[
      ],
      setup_requires=['pytest-runner'],
      tests_require=[
          'pytest==5.2.2',
      ],
      dependency_links=[])
