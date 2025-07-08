
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import OpLogs
from info2soft.common.v20250630.OpLogs import OpLogs
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


class OpLogsTestCase(unittest.TestCase):
    def setUp(self):
        """在每个测试方法运行前执行"""
        self.original_cwd = os.getcwd()
        # 获取当前测试文件的目录
        test_dir = os.path.dirname(os.path.abspath(__file__))
        # 切换工作目录到测试文件所在的目录
        os.chdir(test_dir)

    def tearDown(self):
        """在每个测试方法运行后执行"""
        # 恢复原始工作目录，避免影响其他测试
        os.chdir(self.original_cwd)

    def testListOpLog(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'end': 1548950400,
            'limit': 10,
            'start': 1546272000,
            'op_type': 'delete_nodes',
            'level': 0,
            'description': 'delete_nodes',
            'suffix': '.txt',
            'address': '',
            'username': '',
            'download': False,
        }
        
        
        opLogs = OpLogs(a)
        r = opLogs.listOpLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OpLogs', 'listOpLog', body)

    def testImportOpLog(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        opLogs = OpLogs(a)
        r = opLogs.importOpLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OpLogs', 'importOpLog', body)

    def testDownloadOpLog(self):
        a = Auth(username, pwd)
        body = {
            'end_time': 1,
            'start_time': 1,
            'download': 'true',
        }
        
        
        opLogs = OpLogs(a)
        r = opLogs.downloadOpLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OpLogs', 'downloadOpLog', body)

    def testListUserLog(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'start': 1546272000,
            'end': 1548950400,
            'op_type': 'delete_nodes',
            'level': 0,
            'description': 'delete_nodes',
            'suffix': '.txt',
        }
        
        
        opLogs = OpLogs(a)
        r = opLogs.listUserLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OpLogs', 'listUserLog', body)


if __name__ == '__main__':
    unittest.main()
