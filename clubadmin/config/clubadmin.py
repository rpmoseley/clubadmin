'''
This is the configuration file for whole ClubAdmin package and provides general
settings that are shared across all sub-packages.
'''

from .options import DefaultOptions

# Define the database used by the package which cannot be changed once
# used to prepare the initial settings.
DatabaseDriver = 'apsw'

# The default format for how database files will be created rooted
# to the base installation directory of the package as a whole,
# the {pkgname} is replaced by the name of the sub-package in question.
DefaultDatabase = '/data/{pkgname}.db'
