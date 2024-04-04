from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        print("Installing Antoine...")
        install.run(self)
        print("Antoine is successfully installed!")
        print("To hire Antoine, run 'hire antoine now' in your terminal.")

setup(
    name='antoine',
    version='1.9',
    packages=['antoine'],  # 'antoine' is the name of the package
    author='Antoine Bertin',
    author_email='monolok35@gmail.com',
    description='Hiring Antoine is so much fun!',
    url='https://github.com/monolok/antoine/',
    license='MIT',
    entry_points={
        'console_scripts': [
            'hire antoine now=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
    }
)
