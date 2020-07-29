
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import GeneralInterface
# from info2soft.common.v20200722.GeneralInterface import GeneralInterface
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
pwd = '12345678'


class GeneralInterfaceTestCase(unittest.TestCase):

    def testListRpcTask(self):
        a = Auth(username, pwd)
        body = {
        }
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listRpcTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listRpcTask', body)

    def testListVersionHistory(self):
        a = Auth(username, pwd)
        body = {
        }
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listVersionHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listVersionHistory', body)


if __name__ == '__main__':
    unittest.main()
