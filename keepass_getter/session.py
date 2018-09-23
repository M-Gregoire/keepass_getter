import configparser
import os
from . import protocol
from pathlib import Path

class Session(object):
    def __init__(self, key, id_, requestor):
        self.key = key
        self.id_ = id_
        self.requestor = requestor


    @classmethod
    def start(self, config):
        config = configparser.ConfigParser()
        path = Session.getConfigPath()
        config.read(path)
        id_ = config['Session']['ID']
        key = config['Session']['key']
        requestor = protocol.Requestor(config['KeepassHTTP']['url'])
        if not id_ and not key:
            # No previous association. Loading new association
            key, id_ = requestor.getAndSaveNewAssociation(config)
        elif not protocol.testAssociate(id_, key, requestor):
            # Previous association failed. Loading new association
            key, id_ = requestor.getAndSaveNewAssociation(config)

        return self(key, id_, requestor)

    @staticmethod
    def getConfigPath():
        return os.path.join(Path.home(), '.keepass_getter_config')

    def getLogins(self, url):
        return protocol.getLogins(url, self.id_, self.key, self.requestor)
