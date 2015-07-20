from setuptools import setup, find_packages

entry_points = {
    'console_scripts': [
        'pypaint=pypaint.main:main',
    ],
}

setup(
    name="pypaint",
    packages=find_packages(),
    entry_points=entry_points,
)
