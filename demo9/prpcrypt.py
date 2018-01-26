# coding: utf8
import base64


class prp():
    def __init__(self):
        self.key = "oSifj25WE"

    # 加密
    def encrypt(self, text):
        return self.key + base64.encodestring(text)

    # 解密
    def decrypt(self, text):
        return base64.decodestring(text.replace(self.key, ""))
