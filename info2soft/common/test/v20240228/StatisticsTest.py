
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.Statistics import Statistics
# from info2soft.common.v20200722.Statistics import Statistics
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


class StatisticsTestCase(unittest.TestCase):

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
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        statistics = Statistics(a)
        r = statistics.describeStatistics(body, uuid)
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
            'status': ''
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
            'sub_type': '0',
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
            'daily_sw': 1,
            'daily_st': '11:43',
            'OVERVIEW': 1,
            'bak_bk': 1,
            'bak_rc': 1,
            'cmp_all': 1,
            'ffo': 1,
            'rule': 1,
            'vp': 1,
            'ha': '',
            'sys_cdm': '',
            'bb': '',
            'sys_cloud': '',
            'cdm_remote_rep': '',},
            'weekly_report': {
            'weekly_sw': '',
            'weekly_st': '1,00:00',
            'OVERVIEW': 1,
            'bak_bk': 1,
            'bak_rc': 1,
            'cmp_all': 1,
            'ffo': 1,
            'rule': 1,
            'vp': 1,
            'ha': '',
            'sys_cdm': '',
            'bb': '',
            'sys_cloud': '',
            'cdm_remote_rep': '',},
            'monthly_report': {
            'monthly_sw': '',
            'monthly_st': '1,00:00',
            'OVERVIEW': 1,
            'bak_bk': 1,
            'bak_rc': 1,
            'cmp_all': 1,
            'ffo': 1,
            'rule': 1,
            'vp': 1,
            'ha': '',
            'sys_cdm': '',
            'bb': '',
            'sys_cloud': '',
            'cdm_remote_rep': '',},
            'email': 'g.ntooytmk@ftgxjmb.edu',
            'realtime_report': {
            'realtime_sw': 1,
            'bak_bk': 1,
            'bak_rc': 1,
            'cmp_all': 1,
            'ffo': 1,
            'rule': 1,
            'vp': 1,
            'ha': 1,
            'sys_cdm': 1,
            'bb': '',
            'sys_cloud': '',
            'sms_content': '',
            'cdm_remote_rep': '',},
            'hourly_report': {
            'hourly_sw': '',
            'hourly_st': '"00"',
            'OVERVIEW': '',
            'bak_bk': '',
            'bak_rc': '',
            'cmp_all': '',
            'ffo': '',
            'rule': '',
            'vp': '',
            'ha': '',
            'sys_cdm': '',
            'bb': '',
            'sys_cloud': '',
            'cdm_remote_rep': '',},
            'stat_type': '0',
            'phone': '',
            'sms_template': '',
            'sms_switch': '',
            'sms_report_template': '',
            'email_switch': '',
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


if __name__ == '__main__':
    unittest.main()
