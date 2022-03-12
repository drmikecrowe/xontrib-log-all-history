from setuptools import setup

try:
    with open('README.md') as fh:
        LONG_DESC = fh.read()
except (IOError, OSError):
    LONG_DESC = ''

setup(
    name="xontrib-log_all_history",
    version='1.0.0',
    url='https://github.com/drmikecrowe/xontrib-log_all_history',
    license='MIT',
    author='Mike Crowe',
    author_email='drmikecrowe@gmail.com',
    description='History logger for xonsh',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    data_files=[("", ["LICENSE.txt"])],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
