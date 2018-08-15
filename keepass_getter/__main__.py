#!/usr/bin/env python3
import configparser
import os
from . import session

config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
config.read(path)
session = session.Session.start(config)
print('Initial configuration is done.')
