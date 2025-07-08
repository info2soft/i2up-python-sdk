
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import BigdataBackupRule
from info2soft.bigdataBackupRule.v20250630.BigdataBackupRule import BigdataBackupRule
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


class BigdataBackupRuleTestCase(unittest.TestCase):
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

    def testListBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.listBigdataBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'listBigdataBackupRule', body)

    def testCreateBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'data_type': '',
            'biz_grp_list': [],
            'timeout': 1,
            'priority': 1,
            'disable': 1,
            'plat_list': [{
            'plat_uuid': '',},],
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'replica_uuids': [],
            'wk_path': [],
            'mirr_file_check': '',
            'mirr_sync_flag': '',
            'thread_num_max': 1,
            'thread_num_min': 1,
            'hive_bk_type': 1,
            'select_mode': 1,
            'db_exp': '',
            'table_exp': '',
            'partition_exp': '',
            'sel_db': [],
            'sel_tbl': [],
            'sel_part': [],
            'bkup_schedule': [{
            'sched_name': '',
            'backup_type': 1,
            'retention': 1,
            'start_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_one_time': 1,
            'bkup_policy': 1,
            'exclude_days': [
            '2023-06-02',],
            'cron_policies': '',},],
            'effective_time_switch': 1,
            'effective_time': 1,
            'pre_backup_script': '',
            'post_backup_script': '',
            'expire_policy': 1,
            'band_width': '',
            'script_timeout': 1,
            'excl_path': [],
            'file_type_filter_switch': 0,
            'file_type_filter': '',
            'fragment_size': 1,
            'fragment_switch': 1,
            'data_encrypt_compress_switch': 1,
            'data_encrypt_compress_thread_num': 1,
            'data_encrypt_source': 1,
            'data_compress_level': 1,
            'data_encrypt_type': 1,
            'backup_host_list': [{
            'host_uuid': '',},],
            'retry_switch': 1,
            'retry_times': 1,
            'retry_interval': 1,
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.createBigdataBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'createBigdataBackupRule', body)

    def testModifyBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.modifyBigdataBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'modifyBigdataBackupRule', body)

    def testDescribeBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.describeBigdataBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'describeBigdataBackupRule', body)

    def testListBigdataBackupRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.listBigdataBackupRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'listBigdataBackupRuleStatus', body)

    def testManualStartBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'manual_start',
            'plat_list': [{
            'rule_uuid': '2F343194-2AE6-4583-A8C1-5EAC23203766',
            'platform_uuid': '840D24E3-C594-46CC-BC5C-C57C291773B6',
            'host_uuid': '7D265778-8917-42DF-A5C9-7E2C91E31EBF',},],
            'sched_name': 'full',
            'rule_uuids': [
            '2F343194-2AE6-4583-A8C1-5EAC23203766',],
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.manualStartBigdataBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'manualStartBigdataBackupRule', body)

    def testDisableBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'manual_start',
            'plat_list': [{
            'rule_uuid': '2F343194-2AE6-4583-A8C1-5EAC23203766',
            'platform_uuid': '840D24E3-C594-46CC-BC5C-C57C291773B6',
            'host_uuid': '7D265778-8917-42DF-A5C9-7E2C91E31EBF',},],
            'sched_name': 'full',
            'rule_uuids': [
            '2F343194-2AE6-4583-A8C1-5EAC23203766',],
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.disableBigdataBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'disableBigdataBackupRule', body)

    def testEnableBigdataBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'manual_start',
            'plat_list': [{
            'rule_uuid': '2F343194-2AE6-4583-A8C1-5EAC23203766',
            'platform_uuid': '840D24E3-C594-46CC-BC5C-C57C291773B6',
            'host_uuid': '7D265778-8917-42DF-A5C9-7E2C91E31EBF',},],
            'sched_name': 'full',
            'rule_uuids': [
            '2F343194-2AE6-4583-A8C1-5EAC23203766',],
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.enableBigdataBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'enableBigdataBackupRule', body)

    def testListBigdataBackupRuleBakHistory(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': '',
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.listBigdataBackupRuleBakHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'listBigdataBackupRuleBakHistory', body)

    def testListBigdataBackupRuleHiveTableInfo(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': '',
            'table_name': '',
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.listBigdataBackupRuleHiveTableInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'listBigdataBackupRuleHiveTableInfo', body)

    def testListBigdataBackupRuleHivePartitionInfo(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': '',
            'table_name': '',
            'partition_name': '',
        }
        
        
        bigdataBackupRule = BigdataBackupRule(a)
        r = bigdataBackupRule.listBigdataBackupRuleHivePartitionInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataBackupRule', 'listBigdataBackupRuleHivePartitionInfo', body)


if __name__ == '__main__':
    unittest.main()
