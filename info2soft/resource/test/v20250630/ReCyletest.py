
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ReCyle
from info2soft.resource.v20250630.ReCyle import ReCyle
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


class ReCyleTestCase(unittest.TestCase):
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

    def testListRecycle(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'type': '',
            'where_args': {
            'xxx': '',},
        }
        
        
        reCyle = ReCyle(a)
        r = reCyle.listRecycle(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ReCyle', 'listRecycle', body)

    def testDeleteRecycle(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        reCyle = ReCyle(a)
        r = reCyle.deleteRecycle(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ReCyle', 'deleteRecycle', body)

    def testListRecycleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'fD7422B8-6652-843f-B6ce-E8e7DDc3b791',],
            'force_refresh': 0,
        }
        
        
        reCyle = ReCyle(a)
        r = reCyle.listRecycleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ReCyle', 'listRecycleStatus', body)


if __name__ == '__main__':
    unittest.main()
