import rsa
import os
import base64


class Rsa(object):
    def __init__(self):
        self

    # rsa加密
    def rsaEncrypt(self, pwd):
        path = os.path.abspath(os.path.dirname(os.getcwd())) + '\common\public_key.pem'
        with open(path, 'r') as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(p)
        code = rsa.encrypt(pwd.encode('utf-8'), pubkey)
        code = base64.b64encode(code).decode('utf-8')
        return code
