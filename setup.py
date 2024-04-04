from setuptools import setup

# Print a message before installation
print("Installing Antoine...")

setup(
    name='antoine',
    version='0.2',
    author='Antoine Bertin',
    author_email='monolok35@gmail.com',
    include_package_data=True,
    install_requires=[],
    url='https://github.com/monolok/antoine',
    license='MIT',
    entry_points={
        'console_scripts': [
            'antoine=antoine.app:main',
        ],
    },
)

# Print a message after installation
print("Antoine is successfully installed!")
print("Let's goooo !")
print("Antoine is a good boy")
