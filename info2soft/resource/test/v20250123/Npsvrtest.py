
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Npsvr
from info2soft.resource.v20250123.Npsvr import Npsvr
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
            'etcd_url_uuid': '',
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
            'etcd_url_uuid': '',
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

    def testNpsvrOperate(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'maintain',
            'npsvr_uuids': [],
            'switch': 0,
        }
        
        
        npsvr = Npsvr(a)
        r = npsvr.npsvrOperate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'npsvrOperate', body)

    def testListConfigItems(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        npsvr = Npsvr(a)
        r = npsvr.listConfigItems(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'listConfigItems', body)

    def testUpdateConfigItems(self):
        a = Auth(username, pwd)
        body = {
            'config_items': [{
            'name': '',
            'value': '',},],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        npsvr = Npsvr(a)
        r = npsvr.updateConfigItems(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Npsvr', 'updateConfigItems', body)


if __name__ == '__main__':
    unittest.main()
