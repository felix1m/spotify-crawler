from setuptools import setup, find_packages

setup(
    name='spotify-crawler',
    version='0.2',
    packages=['crawler'],
    include_package_data=True,
    install_requires=[
        'Click',
        'pyitunes',
        'six',
        'spotipy>=2.3'
    ],
    entry_points={
    'console_scripts': [
        'spotify-crawler=main:cli',
    ],
},
    dependency_links=[
          'git+https://github.com/liamks/pyitunes.git#egg=pyItunes',
      ]
)
