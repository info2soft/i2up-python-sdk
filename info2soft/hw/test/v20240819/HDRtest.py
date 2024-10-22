
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import HDR
from info2soft.hw.v20240819.HDR import HDR
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


class HDRTestCase(unittest.TestCase):

    def testUpdateSetting(self):
        a = Auth(username, pwd)
        body = {
            'hcs_url': '',
        }
        
        
        hDR = HDR(a)
        r = hDR.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'updateSetting', body)

    def testModifyProfile(self):
        a = Auth(username, pwd)
        body = {
            'hcs_username': '',
            'hcs_password': '',
        }
        
        
        hDR = HDR(a)
        r = hDR.modifyProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'modifyProfile', body)

    def testListProfile(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.listProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'listProfile', body)

    def testGetOpLogUsers(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.getOpLogUsers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getOpLogUsers', body)


if __name__ == '__main__':
    unittest.main()
