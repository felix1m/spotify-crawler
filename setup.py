from setuptools import setup, find_packages

setup(
    name='spotify-crawler',
    version='0.2',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        'Click',
        'pyItunes',
        'six',
        'spotipy>=2.3'
    ],
    entry_points={
    'console_scripts': [
        'spotify-crawler=crawler.main:cli',
    ],
},
    dependency_links=[
          'http://github.com/liamks/pyitunes/tarball/master#egg=pyItunes-master'
      ]
)
