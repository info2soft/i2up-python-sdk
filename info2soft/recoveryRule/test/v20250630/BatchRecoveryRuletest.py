
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import BatchRecoveryRule
from info2soft.recoveryRule.v20250630.BatchRecoveryRule import BatchRecoveryRule
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


class BatchRecoveryRuleTestCase(unittest.TestCase):
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

    def testListRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': 15,
            'search_field': 'rule_name',
            'search_value': '',
            'direction': '',
            'order_by': '',
            'page': 1,
            'where_args': {
            'task_name': '',},
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.listRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'listRestoreWizardRule', body)

    def testListRestoreWizardRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.listRestoreWizardRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'listRestoreWizardRuleStatus', body)

    def testCreateRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'wk_data_type': 1,
            'task_type': 1,
            'restore_type': 1,
            'priority': 1,
            'auto_start': 1,
            'start_time': 1,
            'bk_set_uuids': [],
            'pattern': '',
            'bk_server_uuid': '',
            'bk_server_addr': '',
            'recover_bk_server': 1,
            'wk_uuid': '',
            'rc_path_policy': 1,
            'wk_path': '',
            'biz_grp_list': [],
            'trans_mode': 1,
            'timeout': 1,
            'thread_num_max': 1,
            'thread_num_min': 1,
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'compress_switch': 1,
            'compress': 1,
            'encrypt_switch': 1,
            'encrypt': 1,
            'bk_path': [],
            'bucket_uuid': '',
            'sto_uuid': '',
            'dst_type': '',
            'excl_path': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.createRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'createRestoreWizardRule', body)

    def testModifyRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'wk_data_type': 1,
            'task_type': 1,
            'restore_type': 1,
            'priority': 1,
            'auto_start': 1,
            'start_time': 1,
            'bk_set_uuids': [],
            'pattern': '',
            'bk_server_uuid': '',
            'bk_server_addr': '',
            'recover_bk_server': 1,
            'wk_uuid': '',
            'rc_path_policy': '',
            'wk_path': '',
            'biz_grp_list': [],
            'trans_mode': 1,
            'timeout': 1,
            'thread_num_max': '',
            'thread_num_min': '',
            'mirr_file_check': '',
            'mirr_sync_flag': '',
            'compress_switch': '',
            'compress': '',
            'encrypt_switch': '',
            'encrypt': '',
            'bk_path': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.modifyRestoreWizardRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'modifyRestoreWizardRule', body)

    def testRegenerateRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.regenerateRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'regenerateRestoreWizardRule', body)

    def testRestoreRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.restoreRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'restoreRestoreWizardRule', body)

    def testStartRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.startRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'startRestoreWizardRule', body)

    def testStopRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.stopRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'stopRestoreWizardRule', body)

    def testDeleteRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
            'force': False,
            'task_uuids': [],
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.deleteRestoreWizardRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'deleteRestoreWizardRule', body)

    def testDownloadRestoreWizardList(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.downloadRestoreWizardList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'downloadRestoreWizardList', body)

    def testDescribeRestoreWizardRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        batchRecoveryRule = BatchRecoveryRule(a)
        r = batchRecoveryRule.describeRestoreWizardRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchRecoveryRule', 'describeRestoreWizardRule', body)


if __name__ == '__main__':
    unittest.main()
