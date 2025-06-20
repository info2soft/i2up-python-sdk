
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import SensMap
from info2soft.stream.v20250630.SensMap import SensMap
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


class SensMapTestCase(unittest.TestCase):
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

    def testDescriptMap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensMap = SensMap(a)
        r = sensMap.descriptMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'descriptMap', body)

    def testListMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.listMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'listMap', body)

    def testCreateMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
            'src_type': '',
            'src_path': '',
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.createMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'createMap', body)

    def testModifyMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
            'src_type': '',
            'src_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensMap = SensMap(a)
        r = sensMap.modifyMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'modifyMap', body)

    def testDeleteMap(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.deleteMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'deleteMap', body)

    def testCreateDbMap(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
            'map_name': '',
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.createDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'createDbMap', body)

    def testListDbMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.listDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'listDbMap', body)

    def testDeleteDbMap(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        sensMap = SensMap(a)
        r = sensMap.deleteDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'deleteDbMap', body)

    def testModifyDbMap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensMap = SensMap(a)
        r = sensMap.modifyDbMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensMap', 'modifyDbMap', body)


if __name__ == '__main__':
    unittest.main()
