#!/usr/bin/env python3
"""
Setup script for Ping Application
"""

from setuptools import setup, find_packages
import os

# Lê o README para usar como long_description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Lê a versão do __init__.py
def get_version():
    with open("src/__init__.py", "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
    return "0.1.0"

setup(
    name="ping-app",
    version=get_version(),
    author="synth1s",
    author_email="your.email@example.com",
    description="Um aplicativo Python simples que implementa funcionalidades básicas de ping/pong",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/synth1s/ping",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Dependências do projeto (se houver)
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "ping-app=src.core:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
