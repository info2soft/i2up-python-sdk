from info2soft import https
from info2soft import config
import linecache
import os


def getToken(username, pwd):
    token = ''
    ssoToken = ''
    res = None
    path = os.path.split(os.path.realpath(__file__))[0] + '/token.txt'
    lists = linecache.getlines(path)
    # 鉴定 token.txt 不为空
    if len(lists) != 0:
        token = lists[0].strip('\n')
        ssoToken = lists[1].strip('\n')
    url = '{0}/auth/token'.format(config.get_default('default_api_host'))
    data = {
        'access_token': ssoToken
    }
    res = https._get(url, data)
    if res[0]['data']['code'] != 0 is None or token == '':
        url = '{0}/auth/token'.format(config.get_default('default_api_host'))
        data = {
            'username': username,
            'pwd': pwd
        }
        r = https._post(url, data)
        token = r[0]['data']['token']
        ssoToken = r[0]['data']['sso_token']
        with open(path, mode='r+', encoding='UTF-8') as tokenFile:
            tokenFile.write(token + '\n' + ssoToken)
            tokenFile.close()
    return [token, ssoToken]



