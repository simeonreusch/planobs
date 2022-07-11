DESCRIPTION = "Plan observations with the Zwicky Transient Facility"
LONG_DESCRIPTION = """Plan observations with the Zwicky Transient Facility. Automated parsing of GCN is only implemented for IceCube at the moment."""

DISTNAME = "planobs"
AUTHOR = "Simeon Reusch"
MAINTAINER = "Simeon Reusch"
MAINTAINER_EMAIL = "simeon.reusch@desy.de"
URL = "https://github.com/simeonreusch/planobs/"
LICENSE = "BSD (3-clause)"
DOWNLOAD_URL = "https://github.com/simeonreusch/planobs/archive/v0.4.2.tar.gz"
VERSION = "0.4.2"

try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup

    raise Exception("Please install python3 setuptools")


if __name__ == "__main__":

    install_requires = [
        "astropy",
        "astroquery",
        "coveralls",
        "numpy",
        "astroplan>=0.7",
        "pandas",
        "penquins",
        "matplotlib",
        "flask",
        "ztfquery==1.18.2",
        "lxml",
        "html5lib",
        "shapely",
        "geopandas",
        "tqdm",
        "typing_extensions",
    ]

    setup(
        name=DISTNAME,
        author=AUTHOR,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=find_packages(),
        classifiers=[
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: BSD License",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ],
    )
