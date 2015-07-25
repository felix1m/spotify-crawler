from setuptools import setup, find_packages

setup(
    name='spotify-crawler',
    version='0.2',
    packages=['crawler'],
    include_package_data=True,
    install_requires=[
        'Click',
        'pyItunes',
        'six',
        'spotipy>=2.3'
    ],
    entry_points={
    'console_scripts': [
        'spotify-crawler=main:cli',
    ],
},
    dependency_links=[
          '"git+ssh://git@github.com/liamks/pyItunes.git@master#egg=pyItunes',
      ]
)
