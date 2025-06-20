
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Dir
from info2soft.common.v20250630.Dir import Dir
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


class DirTestCase(unittest.TestCase):
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

    def testListDir(self):
        a = Auth(username, pwd)
        body = {
            'show_file': 1,
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'dev': 0,
            'path': '',
            'rep_uuid': '',
            'bs_time': '2018-10-23_13-23-08',
            'host_uuid': '',
            'sto_uuid': '',
            'for_vp_file_rc': 1,
            'ftp_uuid': '',
            'cred_uuid': '',
            'auth_user': '',
            'auth_key': '',
            'for_big_data': 1,
            'mscs_group_ip': '',
            'vm_name': '',
            'cluster_config_path': '',
            'page': 1,
            'type': 'bk_snap',
            'mount_dir': '',
            'mount_uuid': '',
            'bk_path': '',
            'rc_point_in_time': '',
            'marker': '',
            'protocol': '',
            'fc_initiator_wwpn': '',
            'fc_target_wwpn': '',
            'timepoint': 1,
            'mapper_path': '',
            'bk_type': 'service_type',
            'task_uuid': '',
            'volume_uuid': '',
            'bucket': '',
            'is_ssl': 1,
            'pool_uuid': '',
            'bk_storage': '',
            'dedupe_uuid': '',
            'is_history_rc': 0,
            'platform_uuid': '',
            'for_dmdsc': 1,
            'instance_uuid': '',
        }
        
        
        dir = Dir(a)
        r = dir.listDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listDir', body)

    def testListDir2(self):
        a = Auth(username, pwd)
        body = {
            'config_port': '26821',
            'os_user': 'chenky',
            'path': '/',
            'config_addr': '192.168.72.76',
            'show_file': 1,
            'os_pwd': '123qwe',
            'proxy_id': '',
            'for_vp_file_rc': 1,
            'proxy_switch': 0,
            'use_credential': 0,
            'cred_uuid': '',
            'is_ssl': 1,
        }
        
        
        dir = Dir(a)
        r = dir.listDir2(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listDir2', body)

    def testCreateDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'A608F04B-0CA4-2ECD-794C-5AFD4580E5B9',
            'path': 'C:\\test2\\12347\\',
            'type': 'bigdata_wk',
        }
        
        
        dir = Dir(a)
        r = dir.createDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'createDir', body)

    def testCheckDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'path': 'E:\\test2\\',
        }
        
        
        dir = Dir(a)
        r = dir.checkDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'checkDir', body)

    def testDeleteDir(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'path': 'aliyun--oos:/TestDir',
            'names': [{
            'name': '222 - 副本 (2).txt',
            'is_dir': '0',},],
            'host_uuid': '',
            'bucket': '',
        }
        
        
        dir = Dir(a)
        r = dir.deleteDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'deleteDir', body)

    def testDescribeDirDelStatus(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'task_uuid': '',
            'host_uuid': '',
        }
        
        
        dir = Dir(a)
        r = dir.describeDirDelStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'describeDirDelStatus', body)

    def testListEtcdDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'path': '',
        }
        
        
        dir = Dir(a)
        r = dir.listEtcdDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listEtcdDir', body)

    def testOperateDtoDir(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'sto_uuid': '',
            'host_uuid': '',
            'sto_type': '',
            'archive_data_direct': 1,
            'valid_period': 1,
            'rate_type': 1,
            'path': [],
            'names': [{
            'name': '',
            'is_dir': '',},],
        }
        
        
        dir = Dir(a)
        r = dir.operateDtoDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'operateDtoDir', body)

    def testListFileBackupDir(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'rc_data_path': '',
            'bk_storage': 1,
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
            'dedupe_uuid': '',
            'rc_point': '',
            'sto_uuid': '',
            'bucket_name': '',
            'rc_pathlist_response': {
            'bk_path': [],
            'rc_time_point_list': [],
            'bk_data_type': 1,
            'wk_data_type': 1,
            'backup_type': 1,
            'task_uuid': '',
            'blk_direct_copy': '',
            'mount_point': '',},
            'path': '',
        }
        
        
        dir = Dir(a)
        r = dir.listFileBackupDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dir', 'listFileBackupDir', body)


if __name__ == '__main__':
    unittest.main()
