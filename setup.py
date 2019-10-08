from setuptools import setup

setup(name='n2',
      author='Tim Vieira',
      description='Command-line tool for searching and indexing notes.',
      version='1.0',
      install_requires=[
          'arsenal',
#          'path.py',
          'whoosh',
      ],
      dependency_links=[
          'https://github.com/timvieira/arsenal.git',
      ],
      scripts=['n2'],
      #packages=['.'],
)
