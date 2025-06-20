
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import UpMonitor
from info2soft.upmonitor.v20250630.UpMonitor import UpMonitor
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


class UpMonitorTestCase(unittest.TestCase):
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

    def testUpMonitorVpRuleStat(self):
        a = Auth(username, pwd)
        body = {
            'up_uuids': '',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.upMonitorVpRuleStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'upMonitorVpRuleStat', body)

    def testUpMonitorOverall(self):
        a = Auth(username, pwd)
        body = {
            'up_uuids': [],
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.upMonitorOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'upMonitorOverall', body)

    def testListUpMonitorPlatSummary(self):
        a = Auth(username, pwd)
        body = {
            'filter_by_biz_grp': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'up_uuid': '',},
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listUpMonitorPlatSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listUpMonitorPlatSummary', body)

    def testListStatistics(self):
        a = Auth(username, pwd)
        body = {
            'obj_name': '',
            'time_used_rate': 1,
            'sub_type': 1,
            'sys_name': '',
            'protect_name': '',
            'status': '',
            'type': '',
            'result': 1,
            'wk_uuid': '',
            'bk_uuid': '',
            'other_uuid': '',
            'group_uuid': '',
            'uuid': '',
            'page': 1,
            'end': 1,
            'name': '',
            'limit': 10,
            'start': 1,
            'time_consuming': 1,
            'up_uuids': [],
            'duration_operator': '',
            'duration': 1,
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listStatistics', body)

    def testDownloadStatistics(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'end': 1,
            'name': '',
            'limit': 10,
            'start': 1,
            'status': '',
            'type': '',
            'result': 1,
            'group_uuid': '',
            'uuid': '',
            'statistics_start': 1,
            'statistics_end': 1,
            'src_type': 1,
            'obj_name': '',
            'time_consuming': 1,
            'suffix': '.csv',
            'wk_uuid': '',
            'bk_uuid': '',
            'other_uuid': '',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.downloadStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'downloadStatistics', body)

    def testListUpMonitorRules(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'search_field': '',
            'search_value': '',
            'up_uuid': '',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listUpMonitorRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listUpMonitorRules', body)

    def testListOpLog(self):
        a = Auth(username, pwd)
        body = {
            'op_type': 'delete_nodes',
            'level': 0,
            'description': 'delete_nodes',
            'suffix': '.txt',
            'address': '',
            'username': '',
            'page': 1,
            'end': 1548950400,
            'limit': 10,
            'start': 1546272000,
            'download': False,
            'up_uuds': [],
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listOpLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listOpLog', body)

    def testListUser(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'up_uuids': [],
            'like_args': {
            'username': '',
            'email': '',
            'mobile': '',},
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listUser', body)

    def testExportUsers(self):
        a = Auth(username, pwd)
        body = {
            'for_import': 0,
            'suffix': 'csv',
            'sub_type': '0',
            'uuids': [],
            'where_args': {
            'timing_type': '',
            'raw_uuid': '',},
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.exportUsers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'exportUsers', body)

    def testAuthUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'oishvmn5YPHJcEDaIjtwd0R9Ug7BN1fk',
            'secret_key': 'fkLiyqsG3P1AzB5jWtYbZa7TU8RN9wSVhe6EldOo',
            'ip': '172.20.2.70',
            'port': '58086',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.authUpMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'authUpMonitor', body)

    def testDescribeUpMonitorToken(self):
        a = Auth(username, pwd)
        body = {
            'up_uuid': 'CE753C48-96F9-6C38-C3DE-A25E7405D03F',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.describeUpMonitorToken(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'describeUpMonitorToken', body)

    def testCreateUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'oishvmn5YPHJcEDaIjtwd0R9Ug7BN1fk',
            'biz_grp_list': [],
            'comment': '备注xxx',
            'secret_key': 'fkLiyqsG3P1AzB5jWtYbZa7TU8RN9wSVhe6EldOo',
            'ip': '172.20.2.70',
            'port': '58086',
            'up_uuid': 'CE753C48-96F9-6C38-C3DE-A25E7405D03F',
            'up_name': '就这个控制机',
            'auditor_access_key': '',
            'sysadmin_access_key': '',
            'sysadmin_secret_key': '',
            'auditor_secret_key': '',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.createUpMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'createUpMonitor', body)

    def testModifyUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'up_name': '就这个控制机',
            'access_key': 'oishvmn5YPHJcEDaIjtwd0R9Ug7BN1fk',
            'secret_key': 'fkLiyqsG3P1AzB5jWtYbZa7TU8RN9wSVhe6EldOo',
            'ip': '172.20.2.70',
            'port': '58086',
            'comment': '备注xxx',
            'biz_grp_list': [],
            'random_str': '11111111-1111-1111-1111-111111111111',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        upMonitor = UpMonitor(a)
        r = upMonitor.modifyUpMonitor(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'modifyUpMonitor', body)

    def testListUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'filter_by_biz_grp': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'up_uuid': '',},
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listUpMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listUpMonitor', body)

    def testDescribeUpMonitor(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        upMonitor = UpMonitor(a)
        r = upMonitor.describeUpMonitor(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'describeUpMonitor', body)

    def testRefreshUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'up_uuids': [
            'CE753C48-96F9-6C38-C3DE-A25E7405D03F',],
            'operate': 'refresh',
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.refreshUpMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'refreshUpMonitor', body)

    def testListUpMonitorStatus(self):
        a = Auth(username, pwd)
        body = {
            'up_uuids': [
            'CE753C48-96F9-6C38-C3DE-A25E7405D03F',],
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.listUpMonitorStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'listUpMonitorStatus', body)

    def testDeleteUpMonitor(self):
        a = Auth(username, pwd)
        body = {
            'up_uuids': [
            'CE753C48-96F9-6C38-C3DE-A25E7405D03F',],
        }
        
        
        upMonitor = UpMonitor(a)
        r = upMonitor.deleteUpMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UpMonitor', 'deleteUpMonitor', body)


if __name__ == '__main__':
    unittest.main()
