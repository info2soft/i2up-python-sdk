
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Diagnose
from info2soft.common.v20250630.Diagnose import Diagnose
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


class DiagnoseTestCase(unittest.TestCase):
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

    def testCreateDiagnose(self):
        a = Auth(username, pwd)
        body = {
            'item_uuid': '',
            'check_type': 1,
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'config_addr': '',
            'config_port': '',
            'start_date': '2022-10-24',
            'end_date': '2022-10-27',
            'time_switch': 0,
        }
        
        
        diagnose = Diagnose(a)
        r = diagnose.createDiagnose(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Diagnose', 'createDiagnose', body)

    def testListDiagnose(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        
        diagnose = Diagnose(a)
        r = diagnose.listDiagnose(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Diagnose', 'listDiagnose', body)

    def testDeleteDiagnose(self):
        a = Auth(username, pwd)
        body = {
            'check_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        diagnose = Diagnose(a)
        r = diagnose.deleteDiagnose(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Diagnose', 'deleteDiagnose', body)

    def testListVpRules(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        diagnose = Diagnose(a)
        r = diagnose.listVpRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Diagnose', 'listVpRules', body)


if __name__ == '__main__':
    unittest.main()
