from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="db1",
    version="0.1.0",
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/db1-io/db1-py",
    project_urls={
        "Source Code": "https://github.com/db1-io/db1-py",
    },
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pyarrow",
        "pandas",
        "protobuf>=4.21.11",
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
