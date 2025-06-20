
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Statistics
from info2soft.common.v20250630.Statistics import Statistics
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


class StatisticsTestCase(unittest.TestCase):
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

    def testListStatistics(self):
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
            'time_used_rate': 1,
            'sub_type': 1,
            'obj_name': '',
            'time_consuming': 1,
            'wk_uuid': '',
            'bk_uuid': '',
            'other_uuid': '',
            'sys_name': '',
            'protect_name': '',
            'chart_filter': 1,
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatistics', body)

    def testDescribeStatistics(self):
        a = Auth(username, pwd)
        body = {
        }
        
        id = 123456
        statistics = Statistics(a)
        r = statistics.describeStatistics(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'describeStatistics', body)

    def testReadStatistics(self):
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
            'time_used_rate': 1,
            'sub_type': '',
            'obj_name': '',
            'time_consuming': 1,
            'wk_uuid': '',
            'bk_uuid': '',
            'other_uuid': '',
        }
        
        
        statistics = Statistics(a)
        r = statistics.readStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'readStatistics', body)

    def testListStatisticsChart(self):
        a = Auth(username, pwd)
        body = {
            'start': 1,
            'sub_type': 'bak_bk',
            'end': 2,
            'type': 'vp',
            'page': 1,
            'limit': 10,
            'timing_only': 0,
            'sys_name': '',
            'protect_name': '',
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatisticsChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatisticsChart', body)

    def testUpdateStatisticsConfig(self):
        a = Auth(username, pwd)
        body = {
            'daily_report': {
            'daily_sw': True,
            'daily_st': '11:43',
            'OVERVIEW': True,
            'bak_bk': True,
            'bak_rc': True,
            'cmp': True,
            'ffo': True,
            'rule': True,
            'vp': True,
            'ha': False,
            'sys_cdm': False,
            'bb': False,
            'sys_cloud': '',
            'cdm_remote_rep': '',
            'timing_work': '',
            'nas_cmp': False,},
            'weekly_report': {
            'weekly_sw': False,
            'weekly_st': '1,00:00',
            'OVERVIEW': True,
            'bak_bk': True,
            'bak_rc': True,
            'cmp': True,
            'ffo': True,
            'rule': True,
            'vp': True,
            'ha': False,
            'sys_cdm': False,
            'bb': False,
            'sys_cloud': '',
            'cdm_remote_rep': '',
            'timing_work': False,
            'nas_cmp': False,},
            'monthly_report': {
            'monthly_sw': False,
            'monthly_st': '1,00:00',
            'OVERVIEW': True,
            'bak_bk': True,
            'bak_rc': True,
            'cmp': True,
            'ffo': True,
            'rule': True,
            'vp': True,
            'ha': False,
            'sys_cdm': False,
            'bb': False,
            'sys_cloud': '',
            'cdm_remote_rep': '',
            'timing_work': False,
            'nas_cmp': False,},
            'email': 'f.jvnhptyb@jkmf.nl',
            'realtime_report': {
            'realtime_sw': True,
            'bak_bk': True,
            'bak_rc': True,
            'cmp': True,
            'ffo': True,
            'rule': True,
            'vp': True,
            'ha': True,
            'sys_cdm': True,
            'bb': False,
            'sys_cloud': '',
            'sms_content': '',
            'cdm_remote_rep': '',
            'timing_work': False,
            'nas_cmp': False,},
            'hourly_report': {
            'hourly_sw': False,
            'hourly_st': '"00"',
            'OVERVIEW': False,
            'bak_bk': False,
            'bak_rc': False,
            'cmp': False,
            'ffo': False,
            'rule': False,
            'vp': False,
            'ha': False,
            'sys_cdm': False,
            'bb': False,
            'sys_cloud': '',
            'cdm_remote_rep': '',
            'timing_work': '',
            'nas_cmp': False,},
            'stat_type': '0',
            'phone': '',
            'sms_template': '',
            'sms_switch': False,
            'sms_report_template': '',
            'email_switch': False,
            'platform_switch': '',
        }
        
        
        statistics = Statistics(a)
        r = statistics.updateStatisticsConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'updateStatisticsConfig', body)

    def testListStatisticsConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatisticsConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatisticsConfig', body)

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
            'wk_uuid': '',
            'bk_uuid': '',
            'other_uuid': '',
            'suffix': '.csv',
        }
        
        
        statistics = Statistics(a)
        r = statistics.downloadStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'downloadStatistics', body)

    def testDownloadStatisticsChart(self):
        a = Auth(username, pwd)
        body = {
            'start': 1,
            'sub_type': '0',
            'end': 2,
            'type': 'vp',
            'page': 1,
            'limit': 10,
            'timing_only': 0,
            'sys_name': '',
            'protect_name': '',
            'suffix': '',
        }
        
        
        statistics = Statistics(a)
        r = statistics.downloadStatisticsChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'downloadStatisticsChart', body)

    def testListStatisticsRuleChart(self):
        a = Auth(username, pwd)
        body = {
            'start': '',
            'end': '',
            'type': '',
            'sub_type': '',
            'page': '',
            'limit': '',
            'task_uuid': '',
            'task_name': '',
            'wk_node_name': '',
            'bk_node_name': '',
            'config_addr': '',
            'total': 1,
            'success': 1,
            'failed': 1,
            'skipped': 1,
            'canceled': 1,
            'filter_by_biz_grp': 1,
            'download': 1,
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatisticsRuleChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatisticsRuleChart', body)

    def testListStatisticsTrendChart(self):
        a = Auth(username, pwd)
        body = {
            'trend_type': 1,
            'type': '',
            'subtype': '',
            'start': '',
            'end': '',
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatisticsTrendChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatisticsTrendChart', body)

    def testListStatisticsDisplayItems(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        statistics = Statistics(a)
        r = statistics.listStatisticsDisplayItems(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'listStatisticsDisplayItems', body)

    def testSetStatisticsDisplayItems(self):
        a = Auth(username, pwd)
        body = {
            'rule': 1,
            'nas_cmp': 1,
            'cmp': 1,
            'ha': 1,
            'dto': 1,
            'bak_bk9': 1,
            'bak_rc9': 1,
            'vp_bk9': 1,
            'vp_rc9': 1,
            'ffo_bk9': 1,
            'ffo_rc9': 1,
            'bb_bk9': 1,
            'bb_rc9': 1,
        }
        
        
        statistics = Statistics(a)
        r = statistics.setStatisticsDisplayItems(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Statistics', 'setStatisticsDisplayItems', body)


if __name__ == '__main__':
    unittest.main()
