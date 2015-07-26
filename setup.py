# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='spotify-crawler',
    version='0.1',
    url='https://github.com/felix1m/spotify-crawler',
    description='automatically create spotify playlists from various sources',
    author='Felix Müller',
    author_email='mueller.fe@gmail.com',
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
