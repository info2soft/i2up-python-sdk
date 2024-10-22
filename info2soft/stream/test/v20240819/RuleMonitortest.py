
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RuleMonitor
from info2soft.stream.v20240819.RuleMonitor import RuleMonitor
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


class RuleMonitorTestCase(unittest.TestCase):

    def testListActiveNodeChart(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'strict': 1,
            'timestamp': 1,
            'start_offset': 1,
            'end_offset': 1,
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.listActiveNodeChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'listActiveNodeChart', body)

    def testListActiveNodeResources(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'status': 'UNKNOWN',
            'timestamp': 1,},],
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.listActiveNodeResources(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'listActiveNodeResources', body)

    def testUpdateNodeDefaultMonitorPath(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'path': '',
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.updateNodeDefaultMonitorPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'updateNodeDefaultMonitorPath', body)

    def testGetSyncRuleMonitorConf(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.getSyncRuleMonitorConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'getSyncRuleMonitorConf', body)

    def testModifySyncRuleMonitorConf(self):
        a = Auth(username, pwd)
        body = {
            'stream_monitor_settings': {
            'stream_monitor_switch': '',
            'stream_monitor_addr': '',
            'stream_monitor_port': '',
            'stream_monitor_default_db': '',
            'stream_monitor_user': '',
            'stream_monitor_pass': '',
            'stream_monitor_interval': 1,
            'stream_monitor_log_save_time': 1,},
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.modifySyncRuleMonitorConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'modifySyncRuleMonitorConf', body)

    def testExportSyncRuleMonitorStat(self):
        a = Auth(username, pwd)
        body = {
            'stat_type': 1,
            'start': 1,
            'end': 1,
            'user': '',
            'table': '',
            'rule_uuid': '',
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.exportSyncRuleMonitorStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'exportSyncRuleMonitorStat', body)

    def testSyncRuleExtractStatistics(self):
        a = Auth(username, pwd)
        body = {
            'start': '',
            'end': '',
            'rule_uuid': '',
            'interval': 1,
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.syncRuleExtractStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'syncRuleExtractStatistics', body)

    def testSyncRuleLoadStatistics(self):
        a = Auth(username, pwd)
        body = {
            'start': '',
            'end': '',
            'rule_uuid': '',
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.syncRuleLoadStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'syncRuleLoadStatistics', body)

    def testSyncRuleTableExtractStatistics(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'start': '',
            'end': '',
            'rule_uuid': '',
            'table': '',
            'user': '',
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.syncRuleTableExtractStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'syncRuleTableExtractStatistics', body)

    def testSyncRuleTableLoadStatistics(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'start': '',
            'end': '',
            'rule_uuid': '',
            'table': '',
            'user': '',
        }
        
        
        ruleMonitor = RuleMonitor(a)
        r = ruleMonitor.syncRuleTableLoadStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleMonitor', 'syncRuleTableLoadStatistics', body)


if __name__ == '__main__':
    unittest.main()
