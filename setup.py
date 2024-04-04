from setuptools import setup

# Print a message before installation
print("Installing Antoine...")

setup(
    name='antoine',
    version='1.6',
    packages=['antoine'],  # 'antoine' is the name of the package
    entry_points={
        'console_scripts': [
            'hireantoinenow=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[],
)

# Print a message after installation
print("Antoine is successfully installed!")
print("Let's goooo !")
print("Antoine is a good boy")
