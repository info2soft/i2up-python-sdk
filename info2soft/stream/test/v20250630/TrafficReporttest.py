
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import TrafficReport
from info2soft.stream.v20250630.TrafficReport import TrafficReport
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


class TrafficReportTestCase(unittest.TestCase):
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

    def testListReportRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }
        
        
        trafficReport = TrafficReport(a)
        r = trafficReport.listReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TrafficReport', 'listReportRule', body)

    def testListReportRuleStatistics(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'search_field': 'rule_name',
            'search_value': 'test',
            'where_args': {
            'rule_uuid': '013bDbc8-7343-1FBb-c71c-7B35CcbbEB8E',
            'task_uuid': '764B16bf-96Ea-7535-D6cf-6B0bf8d3de4e',},
        }
        
        
        trafficReport = TrafficReport(a)
        r = trafficReport.listReportRuleStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TrafficReport', 'listReportRuleStatistics', body)

    def testListReportRuleHistory(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'where_args': {
            'rule_uuid': '4D149dC7-acef-d29e-Fc33-Bc4bDbD6c11E',},
        }
        
        
        trafficReport = TrafficReport(a)
        r = trafficReport.listReportRuleHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TrafficReport', 'listReportRuleHistory', body)


if __name__ == '__main__':
    unittest.main()
