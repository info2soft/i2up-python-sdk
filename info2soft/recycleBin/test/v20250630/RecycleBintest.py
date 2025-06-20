
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import RecycleBin
from info2soft.recycleBin.v20250630.RecycleBin import RecycleBin
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


class RecycleBinTestCase(unittest.TestCase):
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

    def testListRecycleBin(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'type': '',},
        }
        
        
        recycleBin = RecycleBin(a)
        r = recycleBin.listRecycleBin(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecycleBin', 'listRecycleBin', body)

    def testDescribeRecycleBin(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        recycleBin = RecycleBin(a)
        r = recycleBin.describeRecycleBin(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecycleBin', 'describeRecycleBin', body)


if __name__ == '__main__':
    unittest.main()
