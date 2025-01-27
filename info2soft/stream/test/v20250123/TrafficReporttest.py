
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TrafficReport
from info2soft.stream.v20250123.TrafficReport import TrafficReport
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
            'rule_uuid': 'f3E27F45-d0E6-7C8B-2E14-ebBC1Ac7e6Df',
            'task_uuid': '76Add9DE-5C1C-9D1B-7762-Fc1FFdbf5A2b',},
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
            'rule_uuid': 'CC2101eA-ba83-6e2C-5686-79eedA7d1AeC',},
        }
        
        
        trafficReport = TrafficReport(a)
        r = trafficReport.listReportRuleHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TrafficReport', 'listReportRuleHistory', body)


if __name__ == '__main__':
    unittest.main()
