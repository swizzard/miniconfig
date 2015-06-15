"""
A minimal, opinionated config solution
"""
from __future__ import print_function

from utils import get_config, make_config, from_heroku

try:
    config = get_config()
except IOError:
    print("Warning: No config file found")
    config = {}
except ValueError:
    print("Warining: Invalid config file")
    config = {}

