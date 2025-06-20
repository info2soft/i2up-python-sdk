
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import FullMachineCopy
from info2soft.fullMachineCopy.v20250630.FullMachineCopy import FullMachineCopy
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


class FullMachineCopyTestCase(unittest.TestCase):
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

    def testCreateFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 21,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '',
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
            'gateway': '',
            'is_defroute': False,
            'selected': True,},],
            'new_vm_hostname': '',},],
            'create_vm_type': 1,},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 1,
            'node_name': '',
            'node_lic_list': [],
            'node_cache_path': '',
            'node_log_path': '',},
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.createFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'createFullMachineCopy', body)

    def testModifyFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 21,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '',
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
            'gateway': '',
            'is_defroute': False,},],},],},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 1,
            'node_name': '',
            'random_str': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.modifyFullMachineCopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'modifyFullMachineCopy', body)

    def testDeleteFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'force': 1,
            'del_policy': '',
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.deleteFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'deleteFullMachineCopy', body)

    def testDescribeFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.describeFullMachineCopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'describeFullMachineCopy', body)

    def testListFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.listFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'listFullMachineCopy', body)

    def testListFullMachineCopyStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'force_refresh': 0,
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.listFullMachineCopyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'listFullMachineCopyStatus', body)

    def testStartFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.startFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'startFullMachineCopy', body)

    def testStopFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        fullMachineCopy = FullMachineCopy(a)
        r = fullMachineCopy.stopFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FullMachineCopy', 'stopFullMachineCopy', body)


if __name__ == '__main__':
    unittest.main()
