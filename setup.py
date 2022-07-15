import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nuztf",
    version="0.4.2",
    author="Simeon Reusch",
    author_email="simeon.reusch@desy.de",
    description="Plan observations with the Zwicky Transient Facility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD (3-clause)",
    keywords="astronomy astrophysics",
    url="https://github.com/simeonreusch/planobs",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: BSD (3-clause)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8.0",
    install_requires=[
        "astroplan>=0.7",
        "astropy",
        "astroquery",
        "coveralls",
        "flask",
        "geopandas",
        "html5lib",
        "lxml",
        "pandas",
        "penquins",
        "matplotlib",
        "numpy",
        "shapely",
        "tqdm",
        "ztfquery",
    ],
)
