from setuptools import setup

setup(
    name='antoine',
    version='0.1',
    packages=['antoine'],  # 'antoine' is the name of the package
    entry_points={
        'console_scripts': [
            'antoine=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[],
)