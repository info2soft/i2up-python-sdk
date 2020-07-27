
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import CloudBackup
# from info2soft.cloud.v20200722.CloudBackup import CloudBackup
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
pwd = 'Info1234'
    
                
class CloudBackupTestCase(unittest.TestCase):

    def testListDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listDevice(body)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listDevice', body)

    def testCreateBackup(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup': {
            'secret_key': '',
            'mirr_open_type': '0',
            'bkup_one_time': 0,
            'encrypt_switch': '0',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_data_type': 1,
            'bk_path': [],
            'bkup_policy': 2,
            'mirr_file_check': '0',
            'compress': '0',
            'wk_path': [{
            'node_name': '8.180',
            'path_name': 'PhysicalDrive0',
            'path_size': '42944186880',
            'path_attr': '1',
            'node_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',},],
            'group_name': 'test',
            'wk_uuid': [
            '42614852-BB62-1EF7-FED0-D2354BF3149D',],
            'bk_data_type': 1,
            'bkup_schedule': [{
            'sched_day': 24,
            'sched_time': '11:22',
            'sched_every': 2,
            'limit': 41,
            'backup_type': 0,
            'policys': '每天22:00自动执行',
            'backup_type_show': '全备',
            'running_time': '22:00',},],
            'random_str': '11111111-1111-1111-1111-111111111111',},
        }
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.createBackup(body)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createBackup', body)

    def testModifyCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup': {
            'secret_key': '',
            'mirr_open_type': '0',
            'bkup_one_time': 0,
            'encrypt_switch': '0',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_data_type': 1,
            'bk_path': [],
            'bkup_policy': 2,
            'mirr_file_check': '0',
            'compress': '0',
            'wk_path': [{
            'node_name': '8.180',
            'path_name': 'PhysicalDrive0',
            'path_size': '42944186880',
            'path_attr': '1',
            'node_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',},],
            'group_name': 'test',
            'wk_uuid': [
            '42614852-BB62-1EF7-FED0-D2354BF3149D',],
            'bk_data_type': 1,
            'bkup_schedule': [{
            'sched_day': 24,
            'sched_time': '11:22',
            'sched_every': 2,
            'limit': 41,
            'backup_type': 0,
            'policys': '每天22:00自动执行',
            'backup_type_show': '全备',
            'running_time': '22:00',},],
            'random_str': '11111111-1111-1111-1111-111111111111',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.modifyCloudBackup(body, uuid)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'https', body)

    def testDeleteCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': []
        }
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteCloudBackup(body)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteCloudBackup', body)

    def testListCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listCloudBackup(body)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listCloudBackup', body)

    def testOperateCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': ['22D03E06-94D0-5E2C-336E-4BEEC2D28EC4', '22D03E06-94D0-5E2C-336E-4BEEC2D28EC3']
        }
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.operateCloudBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'operateCloudBackup', body)

    def testDescribeBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeBackup(body, uuid)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeBackup', body)


if __name__ == '__main__':
    unittest.main()
