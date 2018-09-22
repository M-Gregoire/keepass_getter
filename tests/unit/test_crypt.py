# -*- coding: utf-8 -*-
import unittest

from keepass_getter import crypto


class TestCrypto(unittest.TestCase):
    def testPad(self):
        self.assertEqual(b'1234\4\4\4\4', crypto.pad('1234', 64))

    def testUnpad(self):
        self.assertEqual(b'1234', crypto.unpad(b'1234\4\4\4\4', 64))

    def testDecryptReversesEncryptForUnicodeSnowman(self):
        data = '☃'
        key = crypto.getRandomKey()
        iv = crypto.getRandomIV()
        enc = crypto.encrypt(data, key, iv)
        dec = crypto.decrypt(enc, key, iv)
        self.assertEqual(data, dec)

    def testEncrypt(self):
        key='eZNUcE1mUHoHoMW40tfRB/DaYvpWGzojDOT7S0AVOQg='
        iv='FE+fTbKvoZjIP48W/yE8Dg=='
        data = crypto.encrypt('Sally sells seashells', key, iv)
        self.assertEqual('aNbyJgtqd33gFfQrYTkobm1xD6UApyC1x7RF32Hy64w=', data)

    def testDecrypt(self):
        key='eZNUcE1mUHoHoMW40tfRB/DaYvpWGzojDOT7S0AVOQg='
        iv='FE+fTbKvoZjIP48W/yE8Dg=='
        data = crypto.decrypt('aNbyJgtqd33gFfQrYTkobm1xD6UApyC1x7RF32Hy64w=', key, iv)
        self.assertEqual('Sally sells seashells', data)

    def testDecryptDictReversesEncryptDict(self):
        data = {1: '☃', 2: ['☃', '☃'], 3: {'☃': 'snowman'}}
        key = crypto.getRandomKey()
        iv = crypto.getRandomIV()
        enc = crypto.encryptDict(data, key, iv)
        dec = crypto.decryptDict(enc, key, iv)
        self.assertEqual(data, dec)
