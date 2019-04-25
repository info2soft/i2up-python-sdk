# -*- coding: utf-8 -*-

from requests.auth import AuthBase

from info2soft.compat import urlparse
from info2soft import https
from info2soft import config
from info2soft.common.Cache import getToken


class Auth(object):
    """安全机制类

    Attributes:
        username: 账号
        pwd: 密码
    """

    def __init__(self, username, pwd):
        """初始化Auth类"""
        self.__checkKey(username, pwd)
        self._username = username
        self._pwd = pwd
        self._token = ''
        self._ssoToken = ''
        self.token()

    def get_username(self):
        return self._username

    def token(self):
        user = self._username
        pwd = self._pwd
        r = getToken(user, pwd)
        self._token = r[0]
        self._ssoToken = r[1]
        return self._token

    def describePhoneCode(self):
        url = '{0}/auth/getPhoneCode'.format(config.get_default('default_api_host'))
        r = https._post(url, None, self)
        return r[0]['data']

    def regAccount(self):
        url = '{0}/auth/register'.format(config.get_default('default_api_host'))
        r = https._post(url)
        return r[0]['data']

    def resetPwd(self):
        url = '{0}/auth/reset/password'.format(config.get_default('default_api_host'))
        r = https._post(url, None, self)
        return r[0]['data']

    def checkLoginStatus(self):
        url = '{0}/auth/token'.format(config.get_default('default_api_host'))
        data = {
            'access_token': self._ssoToken
        }
        r = https._get(url, data, self)
        print(r)
        return r[0]['data']

    def token_of_request(self, url, body=None, content_type=None):
        parsed_url = urlparse(url)
        query = parsed_url.query
        path = parsed_url.path
        data = path
        if query != '':
            data = ''.join([data, '?', query])
        data = ''.join([data, "\n"])

        if body:
            mimes = [
                'application/x-www-form-urlencoded'
            ]
            if content_type in mimes:
                data += body

        return '{0}'.format(self._token)

    @staticmethod
    def __checkKey(username, pwd):
        if not (username and pwd):
            raise ValueError('invalid key')

    def verify_callback(self, origin_authorization, url, body, content_type='application/x-www-form-urlencoded'):
        """回调验证

        Args:
            origin_authorization: 回调时请求Header中的Authorization字段
            url:                  回调请求的url
            body:                 回调请求的body
            content_type:         回调请求body的Content-Type

        Returns:
            返回true表示验证成功，返回false表示验证失败
        """
        token = self.token_of_request(url, body, content_type)
        authorization = 'QBox {0}'.format(token)
        return origin_authorization == authorization


class RequestsAuth(AuthBase):
    def __init__(self, auth):
        self.auth = auth

    def __call__(self, r):
        if r.body is not None and r.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            token = self.auth.token_of_request(r.url, r.body, 'application/x-www-form-urlencoded')
        else:
            token = self.auth.token_of_request(r.url)
        r.headers['Authorization'] = '{0}'.format(token)
        return r