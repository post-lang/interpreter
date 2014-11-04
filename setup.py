#!/usr/bin/python3

# Bootstrap setuptools
import ez_setup
ez_setup.use_setuptools()
del ez_setup

import setuptools
setuptools.setup(
    name='postlang',
    version='1.0.0d0',
    description='The POST language interpreter',

    author='Pietro Albini',
    author_email='pietro@pietroalbini.io',
    url='http://pietroalbini.io',

    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Interpreters',
    ],

    packages=[
        'postlang'
    ],
    zip_safe=False,

    entry_points = {
        'console_scripts': [
            'post = postlang.cli:main',
        ],
    },

    install_requires=[
        # Nothing here yet
    ],
)
