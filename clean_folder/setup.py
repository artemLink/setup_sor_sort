from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    packages=['clean_folder'],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:sort',
        ],
    },
)