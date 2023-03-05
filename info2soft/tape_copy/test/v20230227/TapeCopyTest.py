
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.tape_copy.v20230227.TapeCopy import TapeCopy
# from info2soft.TapeCopy.v20200722.TapeCopy import TapeCopy
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


class TapeCopyTestCase(unittest.TestCase):

    def testListTapeCopy(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        tapeCopy = TapeCopy(a)
        r = tapeCopy.listTapeCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeCopy', 'listTapeCopy', body)

    def testCreateTapeCopy(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'node_uuid': '',
            'src_library_sn': '',
            'dst_library_sn': '',
            'pool_copy': 0,
            'done_export_tape': 0,
            'src_pool_uuid': '',
            'dst_pool_uuid': '',
            'src_slot_info': [],
            'dst_slot_info': [],
            'tape_uuid': '',
        }
        
        tapeCopy = TapeCopy(a)
        r = tapeCopy.createTapeCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeCopy', 'createTapeCopy', body)

    def testDescribeTapeCopy(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        tapeCopy = TapeCopy(a)
        r = tapeCopy.describeTapeCopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeCopy', 'describeTapeCopy', body)

    def testListTapeCopyStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        tapeCopy = TapeCopy(a)
        r = tapeCopy.listTapeCopyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeCopy', 'listTapeCopyStatus', body)

    def testDeleteTapeCopy(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        tapeCopy = TapeCopy(a)
        r = tapeCopy.deleteTapeCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeCopy', 'deleteTapeCopy', body)


if __name__ == '__main__':
    unittest.main()
