from setuptools import setup, find_namespace_packages

setup(
    name='mccann_hub-echo_trail',
    version='0.1.0',
    packages=find_namespace_packages(where='src', include=['mccann_hub.*']),
    install_requires=[
        "python-json-logger>=3.0.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.9",
)

