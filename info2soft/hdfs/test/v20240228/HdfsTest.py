
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.hdfs.v20240228.Hdfs import Hdfs
# from info2soft.hdfs.v20200722.Hdfs import Hdfs
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


class HdfsTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
