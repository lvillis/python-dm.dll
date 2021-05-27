# -*- coding: utf-8 -*-
import re

from distutils.core import setup
from setuptools import find_packages


def main():
    # Get the long description from the README file
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()

    with open(f'{find_packages()[0]}/__version__.py', 'r', encoding='utf-8') as f:
        version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

    setup(
        name='python-dm',
        version=version,
        description='Dm.dll Python Wrapper.',
        long_description=long_description,
        long_description_content_type='text/markdown',

        author='Lvillis',
        author_email='lvillis@outlook.com',

        url='https://github.com/lvillis/python-dm.dll',
        download_url='https://github.com/lvillis/python-dm.dll/releases',

        license='MIT',

        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        packages=find_packages(),
        install_requires=[
            'pywin32'
        ]
    )


if __name__ == '__main__':
    main()
