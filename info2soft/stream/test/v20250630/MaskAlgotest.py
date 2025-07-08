
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import MaskAlgo
from info2soft.stream.v20250630.MaskAlgo import MaskAlgo
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


class MaskAlgoTestCase(unittest.TestCase):
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

    def testCreateAlgo(self):
        a = Auth(username, pwd)
        body = {
            'ava_sens_type': 1,
            'parent_id': 1,
            'algo_name': '',
            'description': '',
            'params': '',
            'sort': '',
        }
        
        
        maskAlgo = MaskAlgo(a)
        r = maskAlgo.createAlgo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskAlgo', 'createAlgo', body)

    def testListAlgos(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        maskAlgo = MaskAlgo(a)
        r = maskAlgo.listAlgos(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskAlgo', 'listAlgos', body)

    def testDescriptAlgo(self):
        a = Auth(username, pwd)
        body = {
        }
        
        id = 123456
        maskAlgo = MaskAlgo(a)
        r = maskAlgo.descriptAlgo(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskAlgo', 'descriptAlgo', body)

    def testAlgoTest(self):
        a = Auth(username, pwd)
        body = {
            'example': {
            'orig': '1231',
            'mask': '-',},
            'parent_id': 308,
            'ava_sens_type': 8,
            'type_arg': '',
            'id': 308,
            'params': [],
        }
        
        
        maskAlgo = MaskAlgo(a)
        r = maskAlgo.algoTest(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskAlgo', 'algoTest', body)


if __name__ == '__main__':
    unittest.main()
