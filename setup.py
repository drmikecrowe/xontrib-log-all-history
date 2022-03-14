#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-log-all-history',
    version='1.1.0',
    license='MIT',
    author='Log All History',
    author_email='drmikecrowe@gmail.com',
    description="persists all shell history in $HOME/.logs",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/drmikecrowe/xontrib-log-all-history',
    project_urls={
        "Documentation": "https://github.com/drmikecrowe/xontrib-log-all-history/blob/master/README.md",
        "Code": "https://github.com/drmikecrowe/xontrib-log-all-history",
        "Issue tracker": "https://github.com/drmikecrowe/xontrib-log-all-history/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
