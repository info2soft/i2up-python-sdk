
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import GeneralSettings
from info2soft.common.v20250630.GeneralSettings import GeneralSettings
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


class GeneralSettingsTestCase(unittest.TestCase):
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

    def testChkEtcdUrl(self):
        a = Auth(username, pwd)
        body = {
            'etcd_url_uuid': '',
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.chkEtcdUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'chkEtcdUrl', body)

    def testCreateUpdateEtcd(self):
        a = Auth(username, pwd)
        body = {
            'user': '',
            'pwd': '',
            'cls_conf': [{
            'ip': '',
            'port': '',},],
            'node_access_list': [{
            'name': '',
            'ip_list': [{
            'ip': '',
            'port': '',},],
            'uuid': '',},],
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.createUpdateEtcd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'createUpdateEtcd', body)

    def testListEtcd(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.listEtcd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'listEtcd', body)

    def testScanEtcdConf(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port': '',
            'user': '',
            'pwd': '',
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.scanEtcdConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'scanEtcdConf', body)

    def testCreateUpdateScheduleSvr(self):
        a = Auth(username, pwd)
        body = {
            'node_access_list': [{
            'ip': '',
            'uuid': '',},],
            'os_pwd': '',
            'os_user': '',
            'rpc_port': '',
            'data_port': '',
            'rpc_addr': '',
            'etcd_url_uuid': '',
            'bkset_meta_data_path': '',
            'log_dir': '',
            'log_save_time': 1,
            'log_save_size': 1,
            'task_schedule_interval_time': 1,
            'bkupset_expire_delay_time': 1,
            'bkupset_expire_check_time': 1,
            'delete_failed_interval_time': 1,
            'max_delete_times': 1,
            'task_timeout_stop_time': 1,
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.createUpdateScheduleSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'createUpdateScheduleSvr', body)

    def testListScheduleSvr(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalSettings = GeneralSettings(a)
        r = generalSettings.listScheduleSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralSettings', 'listScheduleSvr', body)


if __name__ == '__main__':
    unittest.main()
