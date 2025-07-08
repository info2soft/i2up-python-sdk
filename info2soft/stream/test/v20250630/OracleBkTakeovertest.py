
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import OracleBkTakeover
from info2soft.stream.v20250630.OracleBkTakeover import OracleBkTakeover
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


class OracleBkTakeoverTestCase(unittest.TestCase):
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

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'Be473130-Ec0b-b9d2-d7A8-1C4ADc7fDaC4',
            'type': 1,
            'enable_trgjob': 1,
            'enable_alter_seq': 1,
            'start_val': 10,
            'execute_script': 1,
            'enable_attachip': 0,
            'net_adapter': '',
            'ip': '',
            'disable_trgjob': 1,
            'dettach_ip': 1,
            'script_content': '',
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'createBkTakeover', body)

    def testListBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.listBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'listBkTakeover', body)

    def testListBkTakeoverNetworkCard(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.listBkTakeoverNetworkCard(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'listBkTakeoverNetworkCard', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': '525f5ece-83f3-dB7b-3F79-104d58E42393',
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'describeBkTakeoverResult', body)

    def testListSyncBkTakeoverStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'bf0c71AE-6278-dfbe-E4CA-BC1d1Acf352D',],
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.listSyncBkTakeoverStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'listSyncBkTakeoverStatus', body)

    def testDeleteBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
            'force': '',
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'deleteBkTakeover', body)


if __name__ == '__main__':
    unittest.main()
