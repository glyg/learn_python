import os
import sys
import subprocess

from setuptools import setup
from setuptools import find_packages


DISTNAME = 'reporter'
DESCRIPTION = 'Simple reporting tool.'
LONG_DESCRIPTION = ('Simple reporting tool.')
MAINTAINER = 'Human Coders'
MAINTAINER_EMAIL = 'guillaume@example.com'
URL = 'https://github.com/felixquinton/tyssue-taylor'
LICENSE = 'None'
DOWNLOAD_URL = 'https://github.com/glyg/reporter.git'

files = ['*.so*', '*.a*', '*.lib*',
         'config/*/*.json', 'data/*.*']

## Version management copied form numpy
## Thanks to them!
MAJOR               = 0
MINOR               = 0
MICRO               = 1
ISRELEASED          = False
VERSION             = '%d.%d.%s' % (MAJOR, MINOR, MICRO)


if __name__ == "__main__":

    setup(
        name=DISTNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        url=URL,
        license=LICENSE,
        download_url=DOWNLOAD_URL,
        version=VERSION,
        classifiers=["Development Status :: 4 - Beta",
                     "Intended Audience :: Science/Research",
                     "License :: OSI Approved :: MPL v2.0",
                     "Natural Language :: English",
                     "Operating System :: MacOS",
                     "Operating System :: Microsoft",
                     "Operating System :: POSIX :: Linux",
                     "Programming Language :: Python :: 3.6",
#                     "Programming Language :: Python :: Implementation :: CPython",
                     "Topic :: Scientific/Engineering :: Bio-Informatics",
                     "Topic :: Scientific/Engineering :: Medical Science Apps",
                     ],

        packages=find_packages(),
        package_data={'tyssue_taylor': files},
        include_package_data=True,
        zip_safe=False
    )
