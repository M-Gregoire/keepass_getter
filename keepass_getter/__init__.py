import configparser
import os
from .session import Session

def getPassword(url,index=0):
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
    config.read(path)
    session = Session.start(config)
    results = session.getLogins(url)
    return results[index]['Password'].decode('ascii')

def showPassword(url,index=0):
    print(getPassword(url,index))
