
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import BackupDomain
from info2soft.backupDomain.v20250630.BackupDomain import BackupDomain
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


class BackupDomainTestCase(unittest.TestCase):
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

    def testListTargetDomainStorageUnit(self):
        a = Auth(username, pwd)
        body = {
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
            'domain_uuid': '',
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.listTargetDomainStorageUnit(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'listTargetDomainStorageUnit', body)

    def testListTargetDomainStorageUnitStatus(self):
        a = Auth(username, pwd)
        body = {
            'unit_uuids': [],
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.listTargetDomainStorageUnitStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'listTargetDomainStorageUnitStatus', body)

    def testCreateBackupDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_name': '',
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
            'comment': '',
            'unit_uuids': [],
            'schedule_svr_ip': '',
            'unit_addr_list': [{
            'unit_uuid': '',
            'unit_addr': '',},],
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.createBackupDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'createBackupDomain', body)

    def testModifyBackupDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_name': '',
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
            'comment': '',
            'unit_uuids': [],
            'unit_addr_list': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupDomain = BackupDomain(a)
        r = backupDomain.modifyBackupDomain(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'modifyBackupDomain', body)

    def testAuthBackupDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.authBackupDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'authBackupDomain', body)

    def testListBackupDomain(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.listBackupDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'listBackupDomain', body)

    def testDescribeBackupDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_name': '',
            'domain_addr': '',
            'access_key': '',
            'secret_key': '',
            'comment': '',
            'unit_uuids': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupDomain = BackupDomain(a)
        r = backupDomain.describeBackupDomain(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'describeBackupDomain', body)

    def testDeleteBackupDomain(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        backupDomain = BackupDomain(a)
        r = backupDomain.deleteBackupDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupDomain', 'deleteBackupDomain', body)


if __name__ == '__main__':
    unittest.main()
