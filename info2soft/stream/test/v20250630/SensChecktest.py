
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import SensCheck
from info2soft.stream.v20250630.SensCheck import SensCheck
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


class SensCheckTestCase(unittest.TestCase):
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

    def testCreateSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'mask_node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'user': '',
            'tabs': '',
            'row': 100,
            'min': 90,
            'sens_types': '1,2,3,4,5,6,7,8,9,10,12,13,14,15,20',
            'map_type': 'db',
            'mix': 0,
            'white': 1,
            'src_type': '',
            'src_path': '',
            'rule_uuid': '',
            'rule_name': 'adsas',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'type_arg': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.createSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'createSensCheck', body)

    def testModifySensCheck(self):
        a = Auth(username, pwd)
        body = {
            'username': 'admin',
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
            'rule_uuid': 'F895D958-F435-47AC-664D-805BA7DFEE89',
            'rule_name': 'asd',
            'map_type': 'db',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'user': '',
            'tabs': '',
            'row': 100,
            'min': 90,
            'sens_types': '1,2,3,4,5,6,7,8,9,10,12,13,14,15,20',
            'create_time': '1601344305',
            'mask_node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'mix': 0,
            'status': 0,
            'start': '2020-09-29 09:51:45',
            'end': '',
            'white': 1,
            'info': '',
            'type_arg': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensCheck = SensCheck(a)
        r = sensCheck.modifySensCheck(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'modifySensCheck', body)

    def testDeleteSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.deleteSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'deleteSensCheck', body)

    def testStartMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.startMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'startMaskRule', body)

    def testStopMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.stopMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'stopMaskRule', body)

    def testListSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.listSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'listSensCheck', body)

    def testDescriptSensCheck(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensCheck = SensCheck(a)
        r = sensCheck.descriptSensCheck(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'descriptSensCheck', body)

    def testListSensCheckStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.listSensCheckStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'listSensCheckStatus', body)

    def testListSensCheckResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': '',
            'user': '',
            'table': '',
            'limit': 1,
            'page': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sensCheck = SensCheck(a)
        r = sensCheck.listSensCheckResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'listSensCheckResult', body)

    def testListSensCheckIgnoreCol(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'col': '',
        }
        
        
        sensCheck = SensCheck(a)
        r = sensCheck.listSensCheckIgnoreCol(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SensCheck', 'listSensCheckIgnoreCol', body)


if __name__ == '__main__':
    unittest.main()
