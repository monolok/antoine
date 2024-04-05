from setuptools import setup

setup(
    name='antoine',
    version='2.4',
    packages=['antoine'],  # 'antoine' is the name of the package
    author='Antoine Bertin',
    author_email='monolok35@gmail.com',
    description='Hiring Antoine is so much fun!',
    url='https://github.com/monolok/antoine/',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hire_antoine=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[]
)