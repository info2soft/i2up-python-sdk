from OpenSSL import crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5

import os
import base64
from info2soft import config
from info2soft import https


class Rsa(object):
    def __init__(self):
        self

    '''
     * 获取公钥
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getPublicSettings(self):

        url = '{0}/sys/public_settings'.format(config.get_default('default_api_host'))

        res = https._get(url, None)
        return res

    def getPublicKey(self, cer_file_path):
        """
        从证书中提取公钥
        :param cer_file_path: 证书存放路径
        :return: 公钥
        """
        with open(cer_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取 PEM 公钥部分
        start = content.find('-----BEGIN PUBLIC KEY-----')
        end = content.find('-----END PUBLIC KEY-----') + len('-----END PUBLIC KEY-----')
        pem_content = content[start:end]

        # 返回 PEM 格式的公钥
        return pem_content.strip()

    # rsa加密
    def rsaEncrypt(self, pwd):
        pemFilePath = os.path.split(os.path.realpath(__file__))[0] + '/public_key.pem'
        # 首先从控制机获取公钥，拿不到用本地的
        pubSettings = self.getPublicSettings()
        isVersion7 = False
        if (pubSettings is not None and
                len(pubSettings) > 0 and
                'data' in pubSettings[0] and
                'pubKey' in pubSettings[0]['data'] and
                pubSettings[0]['data']['pubKey'] is not None):
            pubkey = pubSettings[0]['data']['pubKey']
        else:
            isVersion7 = True
            pubkey = self.getPublicKey(pemFilePath)
        rsaPubkey = RSA.importKey(pubkey)
        if isVersion7:
            cipherPub = PKCS1_v1_5.new(rsaPubkey)
        else:
            cipherPub = PKCS1_OAEP.new(rsaPubkey)
        code = base64.b64encode(cipherPub.encrypt(pwd.encode(encoding="utf-8"))).decode('utf-8')
        return code
