import requests
import os
from . import crypto
from . import session

def associate(requestor):
    """Send a new encryption key to keepass.
    Waits for user to accept and provide a name for the association.
    Returns:
        key: the new encryption key
        identifier: the name provided by the user
    """
    key = crypto.getRandomKey()
    input_data = {
        'RequestType': 'associate',
        'Key': key
    }
    output = requestor(key, input_data, None, None)
    return key, output['Id']


def testAssociate(id_, key, requestor):
    """Test that keepass has the given identifier and key"""
    input_data = {
        'RequestType': 'test-associate',
    }
    return requestor(key, input_data, id_)


def getLogins(url, id_, key, requestor, print_output=False):
    """Query keepass for entries that match `url`"""
    iv = crypto.getRandomIV()
    input_data = {
        'RequestType': 'get-logins',
        'Url': crypto.encrypt(url, key, iv)
    }
    output = requestor(key, input_data, id_, iv=iv)
    decrypted = [
        crypto.decryptDict(entry, key, output['Nonce'])
        for entry in output.get('Entries', [])
    ]
    return decrypted


class Requestor(object):
    def __init__(self, url):
        self.url = url

    def __call__(self, key, input_data, id_, standard_data=None, iv=None):
        data = self.mergeData(key, input_data, id_, standard_data, iv)
        response = requests.post(self.url, json=data)
        return self.processResponse(response, key)

    def mergeData(self, key, input_data, id_, standard_data=None, iv=None):
        # standard_data can be set to {} so need to explicitly check
        # that it is equal to None
        if standard_data is None:
            iv = iv or crypto.getRandomIV()
            standard_data = {
                'Id': id_,
                'Nonce': iv,
                'Verifier': getVerifier(iv, key)
            }
        return dict(standard_data, **input_data)

    def processResponse(self, response, key):
        if response.status_code != 200:
            raise ValueError('Failed to get a response', response)
        output = response.json()
        if not output['Success']:
            raise ValueError(
                'keepass returned a unsuccessful response', response)

        if not checkVerifier(key, output['Nonce'], output['Verifier']):
            raise ValueError('Failed to verify response', response)
        return output

    def getAndSaveNewAssociation(self, config):
        key, id_ = associate(self)
        config['Session']['ID']=id_
        config['Session']['KEY']=key
        path = session.Session.getConfigPath()
        with open(path, 'w') as configfile:
            config.write(configfile)
        return key, id_

def getVerifier(iv, key):
    return crypto.encrypt(iv, key, iv)


def checkVerifier(key, iv, verifier):
    return verifier == crypto.encrypt(iv, key, iv)
