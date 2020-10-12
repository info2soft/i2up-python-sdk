
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'E:/python-sdk')

import unittest
from info2soft.common.FfoMount import FfoMount
# from info2soft.common.v20200722.FfoMount import FfoMount
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
pwd = 'Info1234'


class FfoMountTestCase(unittest.TestCase):

    def testListCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'page': '',
            'limit': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        ffoMount = FfoMount(a)
        r = ffoMount.listCompareResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'listCompareResult', body)

    def testOperateCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'result_uuids': [],
            'operate': '',
        }
        
        ffoMount = FfoMount(a)
        r = ffoMount.operateCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'operateCompareResult', body)

    def testDeleteCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'result_uuids': [],
        }
        
        ffoMount = FfoMount(a)
        r = ffoMount.deleteCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'deleteCompareResult', body)

    def testViewConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        ffoMount = FfoMount(a)
        r = ffoMount.viewConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'viewConfig', body)


if __name__ == '__main__':
    unittest.main()
