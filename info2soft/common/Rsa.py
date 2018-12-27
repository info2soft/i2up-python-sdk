import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# RSA加密解密

pubkey = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5fU404fG3lxBsT5xzY9DKj71SKR89T0/vXMgXaVNxUzOZWMj
7jk97gqgcl+KghWNs0WtDLSVfSZTpIUEZDd8lAwMNUJ3rgLSeYEFxiYyA1C2jzt1
pGxFQLuPtyMrRtkz1T/WmVjvgxnxrupYofh0blJIrcQdn86UMClxcD7+tPklTORj
d24WVNrCt/x3zjR1oX68RYhhE1uBcVcFxjC0AXDjCiMonN31C981+9lmxr5sXRqF
grp0SmVURjoGnAIq00fqsd3VS5U6SZfNbzj9kvjOsyZDMTSusd33J7sz7ClrZs/2
rYVW4FIrTOtAPqnbLBbsgZB2l0fAzCyzSOlTawIDAQABAoIBADay9vpyEJ7x6Ppl
NSLFUh+pbCUEY2jeUdwZl3hPCsnEtE+vnmtbGF0YEAREr6izwcoD597e0bQ8Oqcm
sN25yRtaJklA70DoEPKv+xSgH0NknphBd4FN88crFktkxTWMEuVF0yEU45wWvsNx
oPWeKOvZDMqwnK9Xry4pnX8qrOGU8pmxzR3TbSyH8iu7CBLnz4f9O41dYfeBYmKb
lMNqzES3w8p9O+I2IQgAWAUQdS2ezQg7Rn2lFMlxjVl6Op4qCIxgWnKXOOQtaTSL
nZvWga4KziXgHfvAojk9xkpvFRylnWRWwaexUCdkTTx4FC06cmYp7Ltrvo+awfdH
kPlTVMECgYEA8zolTrHC1T7QSRIBOvHvbf3x1uMWRCUgIuEigb9MspozWZnpwpAV
XTbWt+uKBwb1NPocT/icZyUpX8OPReRdfY9Gsy4M6T0QXYinjRZ5WZsu/T7wgSN+
ABp+ZU4vD8Aqszm35It0t0rzDxgodx3hU0tu4l3+0pNBgZiTwUyZNEsCgYEA8giw
jQkOJYO4a5BRUv+DRyEEX1b3zDgXcLFxiH5iFMGTi8yH6/ZzHQtAfZStutsxw3Kv
7klXHDIWQQTuksuiZh6Y8OsZM/6E58HLnJjbiF7HNDhZGaIj9AqSkTS3H+xMl1VP
BLWEYid8TEKZbMRAoTkMwaW0QhpeiahU32GlqWECgYAN7bF/PSzEG3HADXjmkD4+
1UEJJj37LwkVFkFsnrDctXnlUqwRSUD/8oj/RUzFND/MhdojNkB2o6kn48ILpZU5
AIBy+Fsi7C1Ive+iY7wVRo69T+Jj8s1fYiUE1iJZy45mbxK50safTHp4zdBbaemi
ZHp4GhvioS4qJrunYSSQ2wKBgQCpZuebbxEVtMHpl1M0Ul5h9HwI9uftaf0OBUQ/
kqW3fV115avkvdQIKg3zV5LZS/3inG0CzRZJR81HqNoKqLh73UKSrRowyB3h0ERg
0KQnKJ8or5+9Tzz23EeFlm3tzAg3i6AI3btQr+5RufOEqz/JGBMTnpUyBx7QHp94
0fGPQQKBgE/RkQ+lHIShnN/A9kSGzw1+LiVWG0rgQW65ykS+8G+UIW+rLHnb6k4+
EzBu06WJU0ruN7Ge+6NhOcozixpYaxwsMxCdKV+m0vXYOY+li0D239XifDODywRF
taivktfzcxa/opByOEcKHY00k4rhYB+5JTpQkBidm6qVZkcK8cUO
-----END RSA PRIVATE KEY-----'''


class Rsa(object):
    def __init__(self):
        self

    def encrypt(self, pwd):
        path = "./public_key.pem"
        publickey = RSA.importKey(open(path, "r").read())
        cipher = Cipher_pkcs1_v1_5.new(publickey)
        text = cipher.encrypt(pwd)
        print(text)
        cipher_text = base64.b64encode(cipher.encrypt(pwd))
        print(cipher_text)
        return cipher_text
