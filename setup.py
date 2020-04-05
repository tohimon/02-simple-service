import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_service",
    version="0.0.1",
    author="Michal Bartusiak",
    author_email="bartusiak.michal@gmail.com",
    description="Simple service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tohimon/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)