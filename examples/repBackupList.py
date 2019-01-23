# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'C:\python_sdk')
from info2soft import RepBackup
from info2soft import Auth

username = 'admin'
pwd = 'Info1234'

a = Auth(username, pwd)
body = {
    'search_value': '',
    'limit': 1,
    'type': 1,
    'page': 1,
    'search_field': '',
}
repBackup = RepBackup(a)
ret, info = repBackup.listRepBackup(body)
if ret is not None:
    print('All is OK')
else:
    print(info) # error message in info