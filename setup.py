# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 et wrap tw=76 :

from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='stickerview',
    version='0.1',
    description='Stickerview Website',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='stickerview django REST',
    author='Tobias Rueetschi',
    author_email='tr@brief.li',
    url='https://github.com/keachi/stickerview',
    license='AGPLv3',
    packages=find_packages(),
    install_requires=[
        'django',
        'djangorestframework',
        'djangorestframework-jsonapi',
        'django-filter',
        'Pillow',
        'pytz',
        'psycopg2',
        'mysqlclient',
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-django',
        ],
    },
    entry_points="""
    [console_scripts]
    stickerview=manage:main
    """
)
