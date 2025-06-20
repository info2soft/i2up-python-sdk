
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import VmCloneVm
from info2soft.vmClone.v20250630.VmCloneVm import VmCloneVm
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


class VmCloneVmTestCase(unittest.TestCase):
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

    def testListVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'status': '',},
        }
        
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.listVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'listVmCloneVm', body)

    def testModifyVmConfig(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '',
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'dns': '',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',},],
            'vm_hostname': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.modifyVmConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'modifyVmConfig', body)

    def testDeleteVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 1,
        }
        
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.deleteVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'deleteVmCloneVm', body)

    def testStartVmVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.startVmVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'startVmVmCloneVm', body)

    def testStopVmVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.stopVmVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'stopVmVmCloneVm', body)

    def testListVmCloneVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'force_refresh': 1,
            'uuids': [
            'F0Bd1A0B-503F-D174-d298-eeF39aBAcfAe',
            'fFbfcBDC-fef1-38d8-0848-F5ECb2D34627',],
        }
        
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.listVmCloneVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'listVmCloneVmStatus', body)

    def testDescribeVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vmCloneVm = VmCloneVm(a)
        r = vmCloneVm.describeVmCloneVm(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneVm', 'describeVmCloneVm', body)


if __name__ == '__main__':
    unittest.main()
