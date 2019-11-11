# -*- coding: utf-8 -*-


import platform

import requests
import json
from requests.auth import AuthBase

import time
import uuid
import random
import struct
import hmac
import hashlib
import urllib.parse

from info2soft.compat import is_py2, is_py3
from info2soft import config
import info2soft.common.Auth
from info2soft import __version__

_sys_info = '{0}; {1}'.format(platform.system(), platform.machine())
_python_ver = platform.python_version()

USER_AGENT = 'info2softPython/{0} ({1}; ) Python/{2}'.format(__version__, _sys_info, _python_ver)


_headers = {
    'User-Agent': USER_AGENT,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'timestamp': '',
    'Authorization': '',
    'Signature': ''
    }


def __return_wrapper(resp):
    if resp.status_code != 200:
        return None, ResponseInfo(resp)
    resp.encoding = 'utf-8'
    ret = resp.json(encoding='utf-8') if resp.text != '' else {}
    return ret, ResponseInfo(resp)


def _post(url, data, auth=None, headers=None, head_config=None):
    try:
        auth_type = 'token' if auth is None else auth.auth_type
        token = '' if auth is None else auth.token
        ak = '' if auth is None else auth.access_key
        # 3eb647b1
        data['_'] = hex(struct.unpack('<I', struct.pack('<f', random.random()))[0])[2:]

        print('_generate_header in')
        header_config = _generate_header(auth_type, token, ak, 'post', url, data['_'])
        print('header_config')
        print(header_config)

        if headers is not None:
            for k, v in headers.items():
                header_config.update({k: v})
        requests.packages.urllib3.disable_warnings()

        data = json.dumps(data)

        r = requests.post(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=header_config,
            timeout=config.get_default('connection_timeout'),
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _get(url, params=None, auth=None):
    try:
        auth_type = 'token' if auth is None else auth.auth_type
        token = '' if auth is None else auth.token
        ak = '' if auth is None else auth.access_key
        # 3eb647b1
        params['_'] = hex(struct.unpack('<I', struct.pack('<f', random.random()))[0])[2:]

        header_config = _generate_header(auth_type, token, ak, 'get', url, params['_'])

        requests.packages.urllib3.disable_warnings()
        r = requests.get(
            url,
            params=params,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            timeout=config.get_default('connection_timeout'),
            headers=header_config,
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _put(url, data, auth=None, headers=None):
    try:
        auth_type = 'token' if auth is None else auth.auth_type
        token = '' if auth is None else auth.token
        ak = '' if auth is None else auth.access_key
        # 3eb647b1
        data['_'] = hex(struct.unpack('<I', struct.pack('<f', random.random()))[0])[2:]

        header_config = _generate_header(auth_type, token, ak, 'put', url, data['_'])

        data = json.dumps(data)

        if headers is not None:
            for k, v in headers.items():
                header_config.update({k: v})
        requests.packages.urllib3.disable_warnings()
        r = requests.put(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=header_config,
            timeout=config.get_default('connection_timeout'),
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _delete(url, data, auth=None, headers=None):
    try:
        auth_type = 'token' if auth is None else auth.auth_type
        token = '' if auth is None else auth.token
        ak = '' if auth is None else auth.access_key
        # 3eb647b1
        data['_'] = hex(struct.unpack('<I', struct.pack('<f', random.random()))[0])[2:]

        header_config = _generate_header(auth_type, token, ak, 'delete', url, data['_'])

        data = json.dumps(data)

        if headers is not None:
            for k, v in headers.items():
                header_config.update({k: v})
        requests.packages.urllib3.disable_warnings()
        r = requests.delete(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=header_config,
            timeout=config.get_default('connection_timeout'),
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


class _TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = '{0}'.format(self.token)
        return r


def _post_with_token(url, data, token):
    return _post(url, data, _TokenAuth(token))


def _post_with_auth(url, data, auth):
    return _post(url, data, info2soft.common.Auth.RequestsAuth(auth))


# def _generate_signature(_, method, url):
#     timestamp = int(round(time.time() * 1000))
#     nonce = uuid.uuid4()
#     sign_str = method.upper() + '\n' + url + '\n' + _ + '\n' + timestamp + '\n' + nonce
#     signature = hmac.new("key", sign_str, digestmod=hashlib.sha256).digest()
#     return signature


def _generate_header(auth_type='token', token='', ak='', method='', url='', _=''):
    timestamp = int(round(time.time() * 1000))/1000
    nonce = uuid.uuid4()
    header_config = {
        'User-Agent': USER_AGENT,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': token if auth_type is 'token' else '',
        'ACCESS-KEY': ak if auth_type is 'ak' else '',
        'timestamp': str(timestamp),
        'nonce': str(nonce),
        'Signature': ''
    }
    url_parse = urllib.parse.urlsplit(url)
    sign_str = method.upper() + '\n' + url_parse.path + '\n' + _ + '\n' + str(timestamp) + '\n' + str(nonce)
    # signature = hmac.new(token, sign_str, digestmod=hashlib.sha256).hexdigest()
    signature_bytes = hmac.new(bytes(token or 'code', encoding='utf-8'),
                               bytes(sign_str, encoding='utf-8'),
                               digestmod=hashlib.sha256).digest()
    signature = signature_bytes.hex().lower()

    header_config['Signature'] = signature

    return header_config


class ResponseInfo(object):
    """HTTP请求返回信息类

    该类主要是用于获取和解析各种请求后的响应包的header和body。

    """

    def __init__(self, response, exception=None):
        """用响应包和异常信息初始化ResponseInfo类"""
        self.__response = response
        self.exception = exception
        if response is None:
            self.status_code = -1
            self.text_body = None
            self.error = str(exception)
        else:
            self.status_code = response.status_code
            self.text_body = response.text
            if self.status_code >= 400:
                ret = response.json() if response.text != '' else None
                if ret is None or ret['error'] is None:
                    self.error = 'unknown'
                else:
                    self.error = ret['error']

    def ok(self):
        return self.status_code == 200

    def need_retry(self):
        if self.__response is None:
            return True
        code = self.status_code
        if (code // 100 == 5 and code != 579) or code == 996:
            return True
        return False

    def connect_failed(self):
        return self.__response is None

    def __str__(self):
        if is_py2:
            return ', '.join(['%s:%s' % item for item in self.__dict__.items()]).encode('utf-8')
        elif is_py3:
            return ', '.join(['%s:%s' % item for item in self.__dict__.items()])

    def __repr__(self):
        return self.__str__()
