#!/usr/bin/env python

"""Setup script for the acpi module distribution."""

from distutils.core import setup

setup (# Distribution meta-data
       name = "acpi",
       version = "0.1.0",
       description = "Module providing of an uniform and platform independent interface to ACPI",
       author = "Tilo Riemer",
       author_email = "riemer@lincvs.org",
       url = "http://www.iapp.de/~riemer/projects/acpi.py/",

       # Description of the modules and packages in the distribution
       package_dir = {'': 'acpi.py'},
       py_modules = ['acpi']
      )
