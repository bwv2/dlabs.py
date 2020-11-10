import setuptools

with open("./README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="dlabs.py",
    version="0.0.1",
    author="itsmewulf",
    author_email="wulf.developer@gmail.com",
    description="A simple, fully asynchronous wrapper for the Discord Labs API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsmewulf/dlabs.py",
    keywords="api-wrapper, http, request, api, wrapper, discord",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)