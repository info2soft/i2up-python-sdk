
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.Dir import Dir
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
    
                
class DirTestCase(unittest.TestCase):

    def testListDir(self):
        a = Auth(username, pwd)
        body = {
            'show_file': 1,
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'dev': 0,
            'path': '',
            'rep_uuid': '',
            'bs_time': ''
        }
        dir = Dir(a)
        r = dir.listDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listDir', body)

    def testCreateDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'path': 'E:\\test2\\',
        }
        dir = Dir(a)
        r = dir.createDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'createDir', body)

    def testCheckDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'path': 'E:\\test2\\',
        }
        dir = Dir(a)
        r = dir.checkDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'checkDir', body)

    def testListDir2(self):
        a = Auth(username, pwd)
        body = {
            'show_file': 1,
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'dev': 0,
            'path': '',
            'rep_uuid': '',
            'bs_time': ''
        }
        dir = Dir(a)
        r = dir.listDir2(body)
        print(r)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listDir2', body)

    def testDeleteDir(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'path': 'aliyun--oos:/TestDir',
            'names': [{
            'name': '222 - 副本 (2).txt',
            'is_dir': '0',},],
            'host_uuid': '',
        }

        dir = Dir(a)
        r = dir.deleteDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'deleteDir', body)

    def testDescribeDirDelStatus(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'task_uuid': '',
            'host_uuid': '',
        }

        dir = Dir(a)
        r = dir.describeDirDelStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'describeDirDelStatus', body)


if __name__ == '__main__':
    unittest.main()  
