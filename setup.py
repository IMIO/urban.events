# -*- coding: utf-8 -*-
"""Installer for the urban.events package."""

from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="urban.events",
    version="1.0.0a3",
    description="Events configuration for Urban",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Affinitic",
    author_email="support@imio.be",
    url="https://github.com/IMIO/urban.events",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/urban.events",
        "Source": "https://github.com/IMIO/urban.events",
        "Tracker": "https://github.com/IMIO/urban.events/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["urban"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "plone.api",
        "plone.app.dexterity",
        "plone.restapi",
        "z3c.jbot",
        "collective.exportimport",
        'enum34',
    ],
    extras_require={
        "test": [
            "plone.app.contenttypes",
            "plone.app.iterate",
            "plone.app.robotframework[debug]",
            "plone.app.testing",
            "plone.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = urban.events.locales.update:update_locale
    """,
)
