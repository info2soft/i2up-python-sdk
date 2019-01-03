import rsa
import os
import base64


class Rsa(object):
    def __init__(self):
        self

    # rsa加密
    def rsaEncrypt(self, pwd):
        pemFilePath = os.path.split(os.path.realpath(__file__))[0] + '/public_key.pem'
        with open(pemFilePath, 'r') as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(p)
        code = rsa.encrypt(pwd.encode('utf-8'), pubkey)
        code = base64.b64encode(code).decode('utf-8')
        return code
