
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Hdfs
from info2soft.hdfs.v20250123.Hdfs import Hdfs
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


class HdfsTestCase(unittest.TestCase):

    def testHdfsSummary(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.hdfsSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'hdfsSummary', body)

    def testCreateHdfs(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 1,
            'src_uuid': '',
            'tgt_uuid': '',
            'src_path': [],
            'dest_path': [],
            'filters': [],
            'src_db': [],
            'dest_db': [],
            'filter_tables': [],
            'sync_type': 0,
            'overwrite': 0,
            'band_width': '',
            'path_mapping_items': [{
            'src_path': '',
            'dest_path': '',},],
            'retry_count': 3,
            'time_interval': 1,
            'batch_count': 1,
            'alarm_threshold': 1,
            'data_agent_switch': 1,
            'data_agent_compress_type': 1,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.createHdfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'createHdfs', body)

    def testModifyHdfs(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 1,
            'src_uuid': '',
            'tgt_uuid': '',
            'src_path': [],
            'dest_path': [],
            'filters': [],
            'src_db': [],
            'dest_db': [],
            'filter_tables': [],
            'sync_type': 0,
            'overwrite': 0,
            'band_width': '',
            'path_mapping_items': [{
            'src_path': '',
            'dest_path': '',},],
            'random_str': '',
            'retry_count': 1,
            'time_interval': 1,
            'batch_count': 1,
            'alarm_threshold': 1,
            'data_agent_switch': 1,
            'data_agent_compress_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfs = Hdfs(a)
        r = hdfs.modifyHdfs(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'modifyHdfs', body)

    def testListHdfs(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 15,
            'page': 1,
            'filter': {
            'and_or': '',
            'rules': [{
            'key': '',
            'value': '',
            'operator': '',},],},
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfs', body)

    def testDescribeHdfs(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfs = Hdfs(a)
        r = hdfs.describeHdfs(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'describeHdfs', body)

    def testDeleteHdfs(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 0,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.deleteHdfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'deleteHdfs', body)

    def testStartHdfs(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.startHdfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'startHdfs', body)

    def testStopHdfs(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.stopHdfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'stopHdfs', body)

    def testListHdfsStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsStatus', body)

    def testCreateHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 2,
            'src_uuid': '',
            'tgt_uuid': '',
            'src_path': [],
            'dest_path': [],
            'filters': [],
            'src_db': [],
            'dest_db': [],
            'filter_tables': [],
            'path_mapping_items': [{
            'src_path': '',
            'dest_path': '',},],
            'cmp_type': 1,
            'include_tables': [],
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.createHdfsCompare(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'createHdfsCompare', body)

    def testModifyHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 2,
            'src_uuid': '',
            'tgt_uuid': '',
            'src_path': [],
            'dest_path': [],
            'filters': [],
            'src_db': [],
            'dest_db': [],
            'filter_tables': [],
            'path_mapping_items': [{
            'src_path': '',
            'dest_path': '',},],
            'cmp_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfs = Hdfs(a)
        r = hdfs.modifyHdfsCompare(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'modifyHdfsCompare', body)

    def testListHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 15,
            'page': 1,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsCompare(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsCompare', body)

    def testDescribeHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfs = Hdfs(a)
        r = hdfs.describeHdfsCompare(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'describeHdfsCompare', body)

    def testDeleteHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 0,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.deleteHdfsCompare(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'deleteHdfsCompare', body)

    def testStartHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.startHdfsCompare(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'startHdfsCompare', body)

    def testStopHdfsCompare(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.stopHdfsCompare(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'stopHdfsCompare', body)

    def testListHdfsCompareStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsCompareStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsCompareStatus', body)

    def testListHdfsCompareHistory(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'rule_uuid': '',
            'search_field': '',
            'search_value': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsCompareHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsCompareHistory', body)

    def testDescribeHdfsCompareHistory(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfs = Hdfs(a)
        r = hdfs.describeHdfsCompareHistory(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'describeHdfsCompareHistory', body)

    def testDeleteHdfsCompareHistory(self):
        a = Auth(username, pwd)
        body = {
            'uuids[]': [],
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.deleteHdfsCompareHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'deleteHdfsCompareHistory', body)

    def testListHdfsCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'uuid': '',
            'search_field': '',
            'search_value': '',
            'order_by': 'diff_name',
            'direction': 'asc',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsCompareResult', body)

    def testListHdfsCompareResultDetail(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'uuid': '',
            'diff_name': '',
        }
        
        
        hdfs = Hdfs(a)
        r = hdfs.listHdfsCompareResultDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hdfs', 'listHdfsCompareResultDetail', body)


if __name__ == '__main__':
    unittest.main()
