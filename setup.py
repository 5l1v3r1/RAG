#!/usr/bin/env python2
from setuptools import setup

setup(
    name = "RAG",
    version = "1",
    author = "Backslash",
    description = "Generate custom shells on the go.",
    keywords = "Shell",
    url = "https://github.com/backslash",
    scripts=['logging','coloredlogs','pyInstaller'],
    # py_modules=['logging','coloredlogs','pyInstaller'],
    install_requires=['logging','coloredlogs','pyInstaller'],
    long_description="Allows for minimal user interaction to create and generate executable reverse shells.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
