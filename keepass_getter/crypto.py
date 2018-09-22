import base64
import os
from . import util

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


KEY_SIZE = 32 # this is in bytes
IV_SIZE = 16
PAD_SIZE = 128 # in bits

def pad(data, size=PAD_SIZE): # size is in bits; 16 bytes = 128 bits
    padder = padding.PKCS7(size).padder()
    if isinstance(data, str):
        data = data.encode('utf-8')
    padded_data = padder.update(data)
    return padded_data + padder.finalize()


def unpad(padded_data, size=PAD_SIZE):
    unpadder = padding.PKCS7(size).unpadder()
    data = unpadder.update(padded_data)
    return data + unpadder.finalize()


def getCipher(key, iv):
    backend = default_backend()
    return Cipher(
        algorithms.AES(base64.b64decode(key)),
        modes.CBC(base64.b64decode(iv)),
        backend
    )


def encrypt(data, key, iv):
    cipher = getCipher(key, iv)
    encryptor = cipher.encryptor()
    p = pad(data)
    res = encryptor.update(p) + encryptor.finalize()
    return str(base64.b64encode(res), 'utf-8')


def decrypt(data, key, iv):
    cipher = getCipher(key, iv)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(base64.b64decode(data)) + decryptor.finalize()
    return str(unpad(padded_data), 'utf-8')


def getRandomBytes(size):
    return base64.b64encode(os.urandom(size))


def getRandomKey():
    return str(getRandomBytes(KEY_SIZE), 'utf-8')


def getRandomIV():
    return str(getRandomBytes(IV_SIZE), 'utf-8')


def encryptDict(dct, key, iv):
    def _encrypt(v):
        return encrypt(v, key, iv)
    return util.jsonMap(_encrypt, dct)


def decryptDict(encrypted_dict, key, iv):
    def _decrypt(v):
        return decrypt(v, key, iv)
    return util.jsonMap(_decrypt, encrypted_dict)
