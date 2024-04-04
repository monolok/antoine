from setuptools import setup

setup(
    name='antoine',
    version='0.1',
    packages=['antoine'],
    entry_points={
        'console_scripts': [
            'my_package=my_package.__main__:main',
        ],
    },
    include_package_data=True,
    install_requires=[],
)