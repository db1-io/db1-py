from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="db1",
    version="0.1.2",
    author="db1",
    author_email="hello@db1.io",
    description="DB1 Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://db1.io",
    project_urls={
        "Source Code": "https://github.com/db1-io/db1-py",
    },
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pyarrow",
        "pandas",
        "protobuf",
        "requests",
        "websocket-client",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["db1=db1._cli.main:main"],
    },
)
