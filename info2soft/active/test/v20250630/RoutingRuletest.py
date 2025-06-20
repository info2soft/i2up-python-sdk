
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import RoutingRule
from info2soft.active.v20250630.RoutingRule import RoutingRule
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


class RoutingRuleTestCase(unittest.TestCase):
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

    def testCreateReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'check_list': {
            'check_type': 1,
            'tb_cmp_list': [],
            'obj_cmp_list': [],
            'rule_list': [],},
            'save_limit': {
            'save_num': '',
            'save_type': '',},
            'policy_config': {
            'policy_type': 1,
            'policies': '',
            'one_time': '',
            'is_interval': 1,},
            'check_window': {
            'check_num': 1,
            'check_type': 1,},
            'ignore_num': 1,
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.createReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'createReportRule', body)

    def testModifyReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'check_list': {
            'check_type': 1,
            'tb_cmp_list': [],
            'obj_cmp_list': [],
            'rule_list': [],},
            'save_limit': {
            'save_num': '',
            'save_type': '',},
            'policy_config': {
            'policy_type': 1,
            'policies': '',},
            'check_window': {
            'check_num': 1,
            'check_type': 1,},
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.modifyReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'modifyReportRule', body)

    def testListReportRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listReportRule', body)

    def testListReportRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listReportRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listReportRuleStatus', body)

    def testDeleteReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.deleteReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'deleteReportRule', body)

    def testOperateReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.operateReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'operateReportRule', body)

    def testListReportRuleHistory(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'rule_uuid': '7BFCcB83-5629-eB73-5a78-E75AbBCE535C',
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listReportRuleHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listReportRuleHistory', body)

    def testModifyStreamRoutingConf(self):
        a = Auth(username, pwd)
        body = {
            'stream_routing_settings': {
            'content_temp_uuid': [],
            'kafka_switch': '',},
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.modifyStreamRoutingConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'modifyStreamRoutingConf', body)

    def testListStreamRoutingConf(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listStreamRoutingConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listStreamRoutingConf', body)

    def testDeleteReportRuleHistory(self):
        a = Auth(username, pwd)
        body = {
            'task_names': [],
            'rule_uuid': '',
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.deleteReportRuleHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'deleteReportRuleHistory', body)

    def testListReportRuleResult(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'rule_uuid': '',
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listReportRuleResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listReportRuleResult', body)

    def testListBizGroupResource(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'subtype': 0,
        }
        
        
        routingRule = RoutingRule(a)
        r = routingRule.listBizGroupResource(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RoutingRule', 'listBizGroupResource', body)


if __name__ == '__main__':
    unittest.main()
