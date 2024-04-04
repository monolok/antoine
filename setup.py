from setuptools import setup

# Print a message before installation
print("Installing Antoine...")

setup(
    name='antoine',
    version='1.8',
    packages=['antoine'],  # 'antoine' is the name of the package
    author='Antoine Bertin',
    author_email='monolok35@gmail.com',
    description='Hiring Antoine is so much fun!',
    url='https://github.com/monolok/antoine/',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hireantoinenow=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[],
)

# Print a message after installation
print("run in terminal : hireantoinenow")