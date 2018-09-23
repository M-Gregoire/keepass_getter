import configparser
import os
from .session import Session
from pathlib import Path

def getPassword(url,index=0):
    config = configparser.ConfigParser()
    path = Session.getConfigPath()
    try:
        with open(path) as f:
            config.readfp(f)
    except IOError:
        generateConfigFile(config, path)
        config.read(path)
    session = Session.start(config)
    results = session.getLogins(url)
    return results[index]['Password']

def showPassword(url,index=0):
    print(getPassword(url,index))

def generateConfigFile(config, path):
    config['KeepassHTTP'] =  {
        'name': 'KeepassHTTP',
        'url': 'http://localhost:19455/',
    }
    config['Session'] =  {
        'id': '',
        'key': '',
    }
    with open(path, 'w') as configfile:
        config.write(configfile)
