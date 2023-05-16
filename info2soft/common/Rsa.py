from OpenSSL import crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import os
import base64


class Rsa(object):
    def __init__(self):
        self

    def getPublicKey(self, cer_file_path):
        """
        从证书中提取公钥
        :param cer_file_path: 证书存放路径
        :return: 公钥
        """
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cer_file_path, 'rb').read())
        res = crypto.dump_publickey(crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8")
        return res.strip()

    # rsa加密
    def rsaEncrypt(self, pwd):
        pemFilePath = os.path.split(os.path.realpath(__file__))[0] + '/public_key.pem'
        pubkey = self.getPublicKey(pemFilePath)
        pubkey = RSA.importKey(pubkey)
        cipher = PKCS1_v1_5.new(pubkey)
        code = base64.b64encode(cipher.encrypt(pwd.encode(encoding="utf-8"))).decode('utf-8')
        return code
