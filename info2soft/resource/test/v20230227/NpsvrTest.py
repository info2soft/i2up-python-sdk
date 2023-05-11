
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.resource.v20230227.Npsvr import Npsvr
# from info2soft.resource.v20200722.Npsvr import Npsvr
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


class NpsvrTestCase(unittest.TestCase):

    def testCreateNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_name': '',
            'config_addr': '',
            'config_port': '',
            'username': '',
            'password': '',
            'maintenance': '',
            'comment': '',
            'cc_ip': '',
        }
        
        npsvr = Npsvr(a)
        r = npsvr.createNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'createNpsvr', body)

    def testAuthNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'config_port': '',
            'username': '',
            'password': '',
        }
        
        npsvr = Npsvr(a)
        r = npsvr.authNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'authNpsvr', body)

    def testListNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': '',
            'page': '',
            'order_by': '',
        }
        
        npsvr = Npsvr(a)
        r = npsvr.listNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'listNpsvr', body)

    def testModifyNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_name': '',
            'config_addr': '',
            'config_port': '',
            'username': '',
            'password': '',
            'maintenance': '',
            'comment': '',
            'cc_ip': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        npsvr = Npsvr(a)
        r = npsvr.modifyNpsvr(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'modifyNpsvr', body)

    def testDeleteNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuids': [],
            'force': 1,
        }
        
        npsvr = Npsvr(a)
        r = npsvr.deleteNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'deleteNpsvr', body)

    def testGetNpsvrStatus(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuids': [],
        }
        
        npsvr = Npsvr(a)
        r = npsvr.getNpsvrStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'getNpsvrStatus', body)

    def testMaintainNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'switch': 0,
            'operate': 'maintain',
            'npsvr_uuid': 'C760f833-A549-acAd-efe6-7ee01d5Ff07f',
        }
        
        npsvr = Npsvr(a)
        r = npsvr.maintainNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'maintainNpsvr', body)

    def testRenewKeyNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'switch': 0,
            'operate': 'renew_key',
            'npsvr_uuid': 'C760f833-A549-acAd-efe6-7ee01d5Ff07f',
        }

        npsvr = Npsvr(a)
        r = npsvr.renewKeyNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'renewKeyNpsvr', body)


if __name__ == '__main__':
    unittest.main()
