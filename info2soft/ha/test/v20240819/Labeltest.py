
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Label
from info2soft.ha.v20240819.Label import Label
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


class LabelTestCase(unittest.TestCase):

    def testCreateLabel(self):
        a = Auth(username, pwd)
        body = {
            'label_name': 'MSSQLSERVER',
            'content': 'SQL Server服务',
        }
        
        
        label = Label(a)
        r = label.createLabel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Label', 'createLabel', body)

    def testModifyLabel(self):
        a = Auth(username, pwd)
        body = {
            'label_name': 'SQL Server服务',
            'label_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        label = Label(a)
        r = label.modifyLabel(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Label', 'modifyLabel', body)

    def testDeleteLabel(self):
        a = Auth(username, pwd)
        body = {
            'label_uuids': [],
        }
        
        
        label = Label(a)
        r = label.deleteLabel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Label', 'deleteLabel', body)

    def testListLabel(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'label_name',
            'search_value': '',
        }
        
        
        label = Label(a)
        r = label.listLabel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Label', 'listLabel', body)


if __name__ == '__main__':
    unittest.main()
