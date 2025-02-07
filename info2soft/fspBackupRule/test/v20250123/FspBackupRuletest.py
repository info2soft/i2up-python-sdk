
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import FspBackupRule
from info2soft.fspBackupRule.v20250123.FspBackupRule import FspBackupRule
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


class FspBackupRuleTestCase(unittest.TestCase):

    def testListFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_value': 'test',
            'search_field': 'rule_name',
            'order_by': 'rule_name',
            'direction': 'DESC',
            'filter_by_biz_grp': 1,
            'status': '',
            'node_name': '',
            'where_args': {
            'rule_uuid': '',},
            'like_args': {
            'rule_name': '',
            'unit_name': '',},
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.listFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'listFspBackupRule', body)

    def testCreateFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 1,
            'biz_grp_list': [],
            'timeout': 1,
            'priority': 1,
            'disable': 1,
            'client_list': [{
            'node_uuid': '',},],
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'replica_uuids': [],
            'trans_mode': 1,
            'wk_path': [{
            'path': 'PhysicalDrive0\\',
            'name': 'PhysicalDrive0',
            'icon': 'folder',
            'size': 42949672960,
            'file': '',
            'attr': 1,
            'leaf': '',
            'subNodes': [],
            'nodeUuid': '0986CDE6-85C6-4D03-8D78-9DD5E367916D',
            'showSize': '40.00 GB',
            'disabled': '',
            'has_policy': '',
            'right_path': '',
            'is_show': '',},],
            'database_switch': 1,
            'database_type': 1,
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': '',
            'table_space': '',
            'timeout': '',},
            'sqlserver_dbagent_param': {
            'timeout': '',},
            'custom_dbagent_param': {
            'pre_snapshot_script': '',
            'post_snapshot_script': '',},
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
            'compress': 1,
            'compress_switch': 0,
            'encrypt_switch': 1,
            'encrypt': 1,
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'band_width': '',
            'block_stor_format': 1,
            'data_encrypt_compress_switch': 1,
            'data_encrypt_compress_thread_num': 1,
            'data_encrypt_source': 1,
            'data_compress_level': 1,
            'data_encrypt_type': 1,
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.createFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'createFspBackupRule', body)

    def testDescribeFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.describeFspBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'describeFspBackupRule', body)

    def testModifyFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_uuid': '',
            'random_str': '',
            'create_time': '',
            'rule_type': '',
            'biz_grp_list': [],
            'timeout': 1,
            'priority': 1,
            'disable': 1,
            'client_list': [{
            'node_uuid': '',},],
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'replica_uuids': [],
            'trans_mode': 1,
            'wk_path': [{
            'path': 'PhysicalDrive0',
            'name': 'PhysicalDrive0',
            'icon': 'folder',
            'size': 42949672960,
            'file': '',
            'attr': 1,
            'leaf': '',
            'subNodes': [],
            'nodeUuid': '0986CDE6-85C6-4D03-8D78-9DD5E367916D',
            'showSize': '40.00 GB',
            'disabled': '',
            'has_policy': '',
            'right_path': '',
            'is_show': '',},],
            'database_switch': 1,
            'database_type': 1,
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': '',
            'table_space': '',
            'timeout': '',},
            'sqlserver_dbagent_param': {
            'timeout': '',},
            'custom_dbagent_param': {
            'pre_snapshot_script': '',
            'post_snapshot_script': '',},
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
            'compress': 1,
            'compress_switch': 0,
            'encrypt_switch': 1,
            'encrypt': 1,
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'band_width': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.modifyFspBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'modifyFspBackupRule', body)

    def testDeleteFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': 0,
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.deleteFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'deleteFspBackupRule', body)

    def testEnableFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'client_list': [{
            'rule_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_rule_name': '',
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.enableFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'enableFspBackupRule', body)

    def testDisableFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'client_list': [{
            'rule_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_rule_name': '',
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.disableFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'disableFspBackupRule', body)

    def testManualStartFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'client_list': [{
            'rule_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_rule_name': '',
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.manualStartFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'manualStartFspBackupRule', body)

    def testCloneFspBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'client_list': [{
            'rule_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_rule_name': '',
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.cloneFspBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'cloneFspBackupRule', body)

    def testListFspBackupRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.listFspBackupRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'listFspBackupRuleStatus', body)

    def testListFspBackupDeviceInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        fspBackupRule = FspBackupRule(a)
        r = fspBackupRule.listFspBackupDeviceInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackupRule', 'listFspBackupDeviceInfo', body)


if __name__ == '__main__':
    unittest.main()
