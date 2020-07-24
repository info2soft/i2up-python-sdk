from info2soft import https
from info2soft import config
import linecache
import os


def getToken(username, pwd):
    token = ''
    ssoToken = ''
    # path = os.path.split(os.path.realpath(__file__))[0] + '/token.dat'
    path = os.sep.join([os.path.split(os.path.realpath(__file__))[0], 'token.dat'])
    lists = linecache.getlines(path)
    code = 0
    # 鉴定 token.txt 不为空
    if len(lists) != 0:
        token = lists[0].strip('\n')
        ssoToken = lists[1].strip('\n')
        url = '{0}/auth/token'.format(config.get_default('default_api_host'))
        data = {
            'access_token': ssoToken
        }
        res = https._get(url, data)
        if res is not None:
            code = res[0]['data']['code']
        else:
            code = -1
    if code != 0 or token == '':
        url = '{0}/auth/token'.format(config.get_default('default_api_host'))
        data = {
            'username': username,
            'pwd': pwd
        }
        r = https._post(url, data)
        if r[0] is not None and r[0]['ret'] is 200 and r[0]['data']['code'] is 0:
            # 密码错误处理
            token = r[0]['data']['token']
            ssoToken = r[0]['data']['sso_token']
            with open(path, mode='w+', encoding='UTF-8') as tokenFile:
                tokenFile.write(token + '\n' + ssoToken)
                tokenFile.close()
        else:
            if r[0] is None:
                print('Can Not Connect Host')
            else:
                print(r[0]['data']['message'])
            exit()
    return [token, ssoToken]



