import io
import os
from pathlib import Path

from setuptools import setup


def read(path):
    path = Path(os.path.dirname(__file__)) / path
    with io.open(path, "r", encoding="utf-8") as f:
        return f.read()


__version__ = "0.4.0"

long_description = read("README.rst")


setup(
    name="j2y",
    url="https://github.com/crate/j2y",
    author="Christian Haudum",
    author_email="christian@christianhaudum.at",
    description="A command line interface for rendering Jinja2 templates.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    platforms=["any"],
    license="Apache License 2.0",
    packages=["j2cli"],
    entry_points={
        "console_scripts": ["j2y = j2cli.cli:main_deprecated", "j2cli = j2cli.cli:main"]
    },
    python_requires=">=3.8",
    version=__version__,
    install_requires=[
        "Jinja2==3.1.2",
        "pyhcl==0.4.5",
        "PyYAML==6.0.1",
        "types-PyYAML==6.0.12.12",
    ],
    extras_require={
        "test": ["pytest>=5.4"],
        "develop": [
            # versions should match with version in pre-commit config
            "flake8==3.8.4",
            "isort==5.12.0",
            "mypy==0.950",
            "black==22.3.0",
        ],
        "docs": ["Sphinx>=1.8,<1.9"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
