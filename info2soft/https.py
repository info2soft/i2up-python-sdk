# -*- coding: utf-8 -*-


import platform

import requests
import json
from requests.auth import AuthBase

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
    'Content-Type': 'application/json'
    }


def __return_wrapper(resp):
    if resp.status_code != 200:
        return None, ResponseInfo(resp)
    resp.encoding = 'utf-8'
    ret = resp.json(encoding='utf-8') if resp.text != '' else {}
    return ret, ResponseInfo(resp)


def _post(url, data, auth=None, headers=None):
    try:
        data = json.dumps(data)
        post_headers = _headers.copy()
        if headers is not None:
            for k, v in headers.items():
                post_headers.update({k: v})
        r = requests.post(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=post_headers,
            timeout=config.get_default('connection_timeout'),
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _get(url, params=None, auth=None):
    try:
        r = requests.get(
            url,
            params=params,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            timeout=config.get_default('connection_timeout'), headers=_headers,
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _put(url, data, auth=None, headers=None):
    try:
        data = json.dumps(data)
        post_headers = _headers.copy()
        if headers is not None:
            for k, v in headers.items():
                post_headers.update({k: v})
        r = requests.put(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=post_headers,
            timeout=config.get_default('connection_timeout'),
            verify=False
        )
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)


def _delete(url, data, auth=None, headers=None):
    try:
        data = json.dumps(data)
        post_headers = _headers.copy()
        if headers is not None:
            for k, v in headers.items():
                post_headers.update({k: v})
        r = requests.delete(
            url,
            data=data,
            auth=info2soft.common.Auth.RequestsAuth(auth) if auth is not None else None,
            headers=post_headers,
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
