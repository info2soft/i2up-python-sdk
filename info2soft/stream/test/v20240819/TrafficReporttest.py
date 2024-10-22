
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TrafficReport
from info2soft.stream.v20240819.TrafficReport import TrafficReport
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
            'rule_uuid': 'A3Cb7DA9-7e0c-BcF7-c4F5-bC9cb23cfc7B',
            'task_uuid': 'dE6180Cb-dCc6-B6d5-2236-D5DfA371aD16',},
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
            'rule_uuid': '1cF77fbd-e260-1e7B-3c60-47b59AED3fA4',},
        }
        
        
        trafficReport = TrafficReport(a)
        r = trafficReport.listReportRuleHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TrafficReport', 'listReportRuleHistory', body)


if __name__ == '__main__':
    unittest.main()
