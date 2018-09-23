#!/usr/bin/env python3
import configparser
import os
from . import session

config = configparser.ConfigParser()
path = session.Session.getConfigPath()
config.read(path)
session = session.Session.start(config)
print('Initial configuration is done.')
