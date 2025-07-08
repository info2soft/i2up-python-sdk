
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import DtoArchive
from info2soft.dto.v20250630.DtoArchive import DtoArchive
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


class DtoArchiveTestCase(unittest.TestCase):
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

    def testListDtoArchive(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'archive_year': '',
            'archive_time_start': 1,
            'archive_time_end': 1,
            'create_time_start': 1,
            'create_time_end': 1,
            'modify_time_start': 1,
            'modify_time_end': 1,
            'delete_time_start': 1,
            'delete_time_end': 1,},],
            'like_args': [{
            'target_path': '',
            'sync_host_name': '',
            'sync_host_ip': '',
            'source_path': '',},],
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.listDtoArchive(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'listDtoArchive', body)

    def testExportDtoArchiveData(self):
        a = Auth(username, pwd)
        body = {
            'id': [],
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.exportDtoArchiveData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'exportDtoArchiveData', body)

    def testGetDtoArchiveYear(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.getDtoArchiveYear(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'getDtoArchiveYear', body)

    def testDownloadDtoArchiveData(self):
        a = Auth(username, pwd)
        body = {
            'ids': [],
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.downloadDtoArchiveData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'downloadDtoArchiveData', body)

    def testRestoreDtoArchiveData(self):
        a = Auth(username, pwd)
        body = {
            'ids': [],
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.restoreDtoArchiveData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'restoreDtoArchiveData', body)

    def testCreateDtoArchiveReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_uuids': '',
            'policy_type': '',
            'range': 1,
            'policies': [{
            'time': '12:00',
            'day': '',
            'month': '',
            'season_month': '',},],
            'mail_switch': 1,
            'mail_address': [{
            'email': '',
            'name': '',},],
            'retain_num': 1,
            'stat_start': '',
            'stat_end': '',
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.createDtoArchiveReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'createDtoArchiveReportRule', body)

    def testModifyDtoArchiveReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_uuids': '',
            'policy_type': '',
            'range': 1,
            'policies': [{
            'time': '12:00',
            'season_month': '',
            'day': '',
            'month': '',},],
            'mail_switch': 1,
            'mail_address': [{
            'email': '',
            'name': '',},],
            'retain_num': 1,
            'rule_uuid': '',
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.modifyDtoArchiveReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'modifyDtoArchiveReportRule', body)

    def testDescribeDtoArchiveReportRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.describeDtoArchiveReportRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'describeDtoArchiveReportRule', body)

    def testDeleteDtoArchiveReportRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.deleteDtoArchiveReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'deleteDtoArchiveReportRule', body)

    def testListDtoArchiveReportRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'search_field': '',
            'search_value': '',
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.listDtoArchiveReportRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'listDtoArchiveReportRule', body)

    def testListDtoArchiveReportHistory(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'where_args': {
            'rule_uuid': '',},
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.listDtoArchiveReportHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'listDtoArchiveReportHistory', body)

    def testListDtoArchiveReportStatistics(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'rule_uuid': '',
            'task_uuid': '',},
        }
        
        
        dtoArchive = DtoArchive(a)
        r = dtoArchive.listDtoArchiveReportStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoArchive', 'listDtoArchiveReportStatistics', body)


if __name__ == '__main__':
    unittest.main()
