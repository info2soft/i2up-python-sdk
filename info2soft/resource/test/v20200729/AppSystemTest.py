
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft.resource.v20200729.AppSystem import AppSystem
# from info2soft.resource.v20200722.AppSystem import AppSystem
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
    
                
class AppSystemTestCase(unittest.TestCase):

    def testSecDirList(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.secDirList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'secDirList', body)

    def testCreateSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
            'pid': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createSecDir', body)

    def testModifySecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifySecDir(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifySecDir', body)

    def testDeleteSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteSecDir', body)

    def testAppSystemList(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'limit': 1,
            'page': 1,
            'search_field': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemList', body)

    def testAppSystemMembersList(self):
        a = Auth(username, pwd)
        body = {
            'rule_type': 1,
            'name': '',
            'os_type': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemMembersList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemMembersList', body)

    def testDescribeAppSystem(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeAppSystem', body)

    def testCreateAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '73412DAD-A7A6-4605-A9FF-081495C8800B',
            'sys_name': '应用系统name',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 0,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'node_uuids': [
            'EA52A961-9883-66FE-188B-D7266AD9594B',
            '09EEA553-C3B8-0D7A-4797-F7A7E2D4FAE1',],
            'vm_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createAppSystem', body)

    def testModifyAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '',
            'sys_name': '',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 1,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'random_str': '',
            'node_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
            'vm_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyAppSystem', body)

    def testDeleteAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'sys_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteAppSystem', body)

    def testGetVmList(self):
        a = Auth(username, pwd)
        body = {
            'where_args[vp_uuid]': '',
            'search_field': 'vm_name',
            'search_value': 'vm_name',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.getVmList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getVmList', body)

    def testRecoveryList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.recoveryList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'recoveryList', body)

    def testRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.recoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'recoveryStatus', body)

    def testResourceView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.resourceView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'resourceView', body)

    def testResourceProtectionCoverage(self):
        a = Auth(username, pwd)
        body = {
            'level_a': 1,
            'level_b': 1,
            'level_c': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.resourceProtectionCoverage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'resourceProtectionCoverage', body)

    def testTaskView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.taskView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'taskView', body)

    def testListStatisticsReport(self):
        a = Auth(username, pwd)
        body = {
            'start_time': '',
            'end_time': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listStatisticsReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listStatisticsReport', body)

    def testBatchTaskList(self):
        a = Auth(username, pwd)
        body = {
            'like_args[xxx]': '',
            'limit': 1,
            'page': 1,
            'type': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.batchTaskList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'batchTaskList', body)

    def testBatchTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'batch_uuids': [],
        }

        appSystem = AppSystem(a)
        r = appSystem.batchTaskStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'batchTaskStatus', body)

    def testStartBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.startBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startBatchTask', body)

    def testStopBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.stopBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopBatchTask', body)

    def testDeleteBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.deleteBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteBatchTask', body)


if __name__ == '__main__':
    unittest.main()
