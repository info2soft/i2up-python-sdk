
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import DtoLifeManagement
from info2soft.resource.v20250630.DtoLifeManagement import DtoLifeManagement
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


class DtoLifeManagementTestCase(unittest.TestCase):
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

    def testCreateDtoLm(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'status': 0,
            'type': 1,
            'prefix': '',
            'lfa_stor': {
            'config_sw': 1,
            'days': 1,},
            'arch_stor': {
            'config_sw': 1,
            'days': 1,},
            'expr_del': {
            'config_sw': 1,
            'days': 1,},
            'sto_uuid': '',
            'host_uuid': '',
            'path': '',
            'rule_id': '',
        }
        
        
        dtoLifeManagement = DtoLifeManagement(a)
        r = dtoLifeManagement.createDtoLm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoLifeManagement', 'createDtoLm', body)

    def testListDtoLm(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'host_uuid': '',
            'path': '',
            'rule_name': '',
        }
        
        
        dtoLifeManagement = DtoLifeManagement(a)
        r = dtoLifeManagement.listDtoLm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoLifeManagement', 'listDtoLm', body)

    def testModifyDtoLm(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'status': 0,
            'type': 1,
            'prefix': '',
            'lfa_stor': {
            'config_sw': '',
            'days': '',},
            'arch_stor': {
            'config_sw': '',
            'days': '',},
            'expr_del': {
            'config_sw': '',
            'days': '',},
            'sto_uuid': '',
            'host_uuid': '',
            'path': '',
        }
        
        
        dtoLifeManagement = DtoLifeManagement(a)
        r = dtoLifeManagement.modifyDtoLm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoLifeManagement', 'modifyDtoLm', body)

    def testOperateDtoLm(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'sto_uuid': '',
            'host_uuid': '',
            'path': '',
            'rule_names': [],
        }
        
        
        dtoLifeManagement = DtoLifeManagement(a)
        r = dtoLifeManagement.operateDtoLm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoLifeManagement', 'operateDtoLm', body)


if __name__ == '__main__':
    unittest.main()
