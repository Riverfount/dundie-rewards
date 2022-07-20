from setuptools import find_packages, setup

setup(
    name='dundie',
    version='0.1.0',
    description='Reward Point System for Dunder Mifflin',
    author='Vicente Marçal',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dundie = dundie.__main__:main'
        ]
    }
)
