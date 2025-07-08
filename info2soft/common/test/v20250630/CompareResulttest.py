
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import CompareResult
from info2soft.common.v20250630.CompareResult import CompareResult
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


class CompareResultTestCase(unittest.TestCase):
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

    def testListCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'page': '',
            'limit': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        compareResult = CompareResult(a)
        r = compareResult.listCompareResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CompareResult', 'listCompareResult', body)

    def testDownloadCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'result_uuids': [],
            'operate': '',
        }
        
        
        compareResult = CompareResult(a)
        r = compareResult.downloadCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CompareResult', 'downloadCompareResult', body)

    def testDeleteCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'result_uuids': [],
        }
        
        
        compareResult = CompareResult(a)
        r = compareResult.deleteCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CompareResult', 'deleteCompareResult', body)

    def testViewConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        compareResult = CompareResult(a)
        r = compareResult.viewConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CompareResult', 'viewConfig', body)

    def testListDiffDetail(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': '',
            'page': 1,
            'limit': 10,
        }
        
        
        compareResult = CompareResult(a)
        r = compareResult.listDiffDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CompareResult', 'listDiffDetail', body)


if __name__ == '__main__':
    unittest.main()
