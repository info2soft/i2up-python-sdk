
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import Client
# from info2soft.common.v20200722.Client import Client
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
    
                
class ClientTestCase(unittest.TestCase):

    def testUpdateSlaveNode(self):
        a = Auth(username, pwd)
        body = {
            'config': '',
        }
        
        client = Client(a)
        r = client.updateSlaveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'updateSlaveNode', body)

    def testGetVirtualPlatforms(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '',
        }
        
        client = Client(a)
        r = client.getVirtualPlatforms(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getVirtualPlatforms', body)

    def testGetVirtualPlatformRules(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [
            '3C334EF3',
            '3C334EF3',],
        }
        
        client = Client(a)
        r = client.getVirtualPlatformRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getVirtualPlatformRules', body)


if __name__ == '__main__':
    unittest.main()
