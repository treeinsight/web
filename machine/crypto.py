# -*- coding: utf-8 -*-

import os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from ti import settings


class MyCrypto():

    def __init__(self):

        # 인코딩에 사용되는 키가 바뀌어버리면, 나중에 디코딩할 수 없는 사태가 발생하므로,
        # 처음부터 Dev환경은 .profile(PythonAnyWhere서버는 .profile과 WSGI설정파일)에
        # CONTENT_KEY 환경변수로 고정시켜버리는 게 필요함

        CONTENT_KEY = settings.CONTENT_KEY
        self.bs = 32
        self.key = hashlib.sha256(CONTENT_KEY.encode()).digest()
        
    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * MyCrypto.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(MyCrypto.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')


def main():
    crypto = MyCrypto()

    encode = crypto.encrypt('kakaka')
    print("'kakaka' is tested..")
    print("encrypt: {}".format(encode))
    decode = crypto.decrypt(encode)
    print("decrypt: {}".format(decode))

    encode = crypto.encrypt('I go to school. It is very cool day!!!')
    print("'I go to school. It is very cool day!!!' is tested..")
    print("encrypt: {}".format(encode))
    decode = crypto.decrypt(encode)
    print("decrypt: {}".format(decode))


if __name__ == "__main__":
    main()
