
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RecycleBin
from info2soft.recycleBin.v20250123.RecycleBin import RecycleBin
from info2soft import Auth
from info2soft.fileWriter import write
from info2soft.compat import is_py2, is_py3

if is_py2:
    import sys
    import StringIO
    import urllib

    # reload(sys)
    sys.setdefaultencoding('utf-8')
    StringIO = StringIO.StringIO
    urlopen = urllib.urlopen
if is_py3:
    import io
    import urllib

    StringIO = io.StringIO
    urlopen = urllib.request.urlopen

username = 'admin'
pwd = 'Info@123'


class RecycleBinTestCase(unittest.TestCase):

    def testListRecycleBin(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'type': '',},
        }
        
        
        recycleBin = RecycleBin(a)
        r = recycleBin.listRecycleBin(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecycleBin', 'listRecycleBin', body)

    def testDescribeRecycleBin(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        recycleBin = RecycleBin(a)
        r = recycleBin.describeRecycleBin(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecycleBin', 'describeRecycleBin', body)


if __name__ == '__main__':
    unittest.main()
