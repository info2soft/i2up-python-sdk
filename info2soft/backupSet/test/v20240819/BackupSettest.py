
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BackupSet
from info2soft.backupSet.v20240819.BackupSet import BackupSet
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


class BackupSetTestCase(unittest.TestCase):

    def testListBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'where_args': {
            'wk_name': '',
            'src_type': '',
            'bk_name': '',
            'bk_rule_name': '',
            'bk_start_tm': '',
            'bk_end_tm': '',
            'storage_unit_name': '',
            'tname': '',
            'delete': '',
            'copy_id': '',
            'bk_type': '',
            'replica_task_sched_name': '',
            'vp_uuid': '',
            'vm_id': '',
            'instance_name': '',
            'db_name': '',
            'backup_method': 1,
            'content_type': 1,
            'wk_uuid': '',
            'vp_type': 1,},
            'stage': [
            '0',
            '1',],
            'like_args': {
            'barcode': '',},
            'show_all_copy': 1,
            'or_where_by_group': '',
            'filter_log': 0,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupSet', body)

    def testListQueryArgsBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'search_value': '',
            'delete': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.listQueryArgsBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listQueryArgsBackupSet', body)

    def testExtendBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'expire_tm': '',
            'bk_set_uuid': '',},],
            'operate': 'extend',
            'force': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.extendBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'extendBackupSet', body)

    def testExpireBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'expire_tm': '',
            'bk_set_uuid': '',},],
            'operate': 'extend',
            'force': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.expireBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'expireBackupSet', body)

    def testSetPrimaryBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'expire_tm': '',
            'bk_set_uuid': '',},],
            'operate': 'extend',
            'force': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.setPrimaryBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'setPrimaryBackupSet', body)

    def testDeleteDbBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.deleteDbBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'deleteDbBackupSet', body)

    def testManualForceDeleteDbBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.manualForceDeleteDbBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'manualForceDeleteDbBackupSet', body)

    def testDeleteBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'bk_set_id': '',
            'bk_rule_uuid': '',
            'copy_id': '',},],
            'delete_from_db': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.deleteBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'deleteBackupSet', body)

    def testCreateBackupSetRepRule(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuids': [],
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'retention_level': '',
            'start_time': 1,
            'encrypt_setting': {
            'encrypt': 1,
            'encrypt_switch': 1,},
            'compress_setting': {
            'compress': 1,
            'compress_switch': 1,},
            'trans_mode': 1,
            'thread_num': 1,
            'concurrent_mode': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.createBackupSetRepRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'createBackupSetRepRule', body)

    def testDescribeBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'bk_set_id': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.describeBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'describeBackupSet', body)

    def testDescribeDeletedBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.describeDeletedBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'describeDeletedBackupSet', body)

    def testDescribeBackupSetCopy(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'search_field': '',
            'search_value': '',
            'bk_set_uuid': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.describeBackupSetCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'describeBackupSetCopy', body)

    def testListBackupSetRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'search_field': 'primary_copy',
            'search_value': '1',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupSetRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupSetRule', body)

    def testValidateBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuids': [],
            'mode': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.validateBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'validateBackupSet', body)

    def testResetPrimaryBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_id': '',
            'bk_rule_uuid': '',
            'expire_tm': 1,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.resetPrimaryBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'resetPrimaryBackupSet', body)

    def testListBackupChain(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'backup_chain_policy': 1,
            'bk_server_uuid': '',
            'bk_server_addr': '',
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupChain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupChain', body)

    def testDrillBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'drill_list': [{
            'bk_set_uuid': '',
            'orch_vm_name': '',
            'scripts': '',
            'scripts_type': 1,
            'new_flavor_id': '',
            'new_network_id': '',
            'new_network_name': '',
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,},],
            'auto_drill': 0,
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.drillBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'drillBackupSet', body)

    def testListSrcClient(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'src_type': '',},
        }
        
        
        backupSet = BackupSet(a)
        r = backupSet.listSrcClient(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listSrcClient', body)


if __name__ == '__main__':
    unittest.main()
