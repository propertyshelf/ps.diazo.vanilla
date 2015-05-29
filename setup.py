# -*- coding: utf-8 -*-
"""Setup for ps.diazo.vanilla package."""

from setuptools import setup, find_packages

version = '0.7'
description = 'Propertyshelf Vanilla Theme.'
long_description = ('\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
]))

install_requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'z3c.jbot',
]

setup(
    name='ps.diazo.vanilla',
    version=version,
    description=description,
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='plone diazo vanilla',
    author='Propertyshelf, Inc.',
    author_email='development@propertyshelf.com',
    url='https://github.com/propertyshelf/ps.diazo.vanilla',
    download_url='http://pypi.python.org/pypi/ps.diazo.vanilla',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['ps', 'ps.diazo'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            'plone.app.testing',
        ],
    ),
    install_requires=install_requires,
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
