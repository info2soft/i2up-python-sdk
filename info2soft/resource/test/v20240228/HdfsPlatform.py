
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import HdfsPlatform
from info2soft.resource.v20240228.HdfsPlatform import HdfsPlatform
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


class HdfsPlatformTestCase(unittest.TestCase):

    def testCreateHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'hdfs_name': '',
            'hdfs_type': '0',
            'config_addr': '',
            'config_port': 1,
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': 0,
            'keytab': '',
            'principal': '',
            'comment': '',
            'hive_switch': 1,
            'hive': {
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': '',
            'keytab': '',
            'principal': '',},
            'bind_lic_list': [],
            'cc_ip_uuid': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.createHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'createHdfsPlatform', body)

    def testModifyHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'hdfs_name': '',
            'hdfs_type': '0',
            'config_addr': '',
            'config_port': 1,
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': 0,
            'keytab': '',
            'principal': '',
            'comment': '',
            'hive_switch': 1,
            'hive': {
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': '',
            'keytab': '',
            'principal': '',},
            'random_str': '',
            'bind_lic_list': [],
            'cc_ip_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.modifyHdfsPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'modifyHdfsPlatform', body)

    def testListHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 15,
            'page': 1,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsPlatform', body)

    def testDescribeHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.describeHdfsPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'describeHdfsPlatform', body)

    def testDeleteHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 0,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.deleteHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'deleteHdfsPlatform', body)

    def testListHdfsPath(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'path': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsPath', body)

    def testListHdfsHiveEntity(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'database': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsHiveEntity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsHiveEntity', body)

    def testAuthBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'os_user': '',
            'os_pwd': '',
            'address': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.authBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'authBigdataBackupHost', body)

    def testBigdataBackupHostDbAuth(self):
        a = Auth(username, pwd)
        body = {
            'db_user': '',
            'db_pwd': '',
            'db_type': 1,
            'db_address': '',
            'db_port': 1,
            'db_name': '',
            'os_user': '',
            'os_pwd': '',
            'address': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.bigdataBackupHostDbAuth(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'bigdataBackupHostDbAuth', body)

    def testCreateBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'host_name': '',
            'address': '',
            'cc_ip_uuid': '',
            'os_user': '',
            'os_pwd': '',
            'db_type': 1,
            'db_address': '',
            'db_user': '',
            'db_pwd': '',
            'dto_switch': 1,
            'dto_address': '',
            'cls_switch': 1,
            'follower_address': '',
            'bind_lic_list': '',
            'db_name': '',
            'db_port': 1,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.createBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'createBigdataBackupHost', body)

    def testListBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listBigdataBackupHost', body)

    def testDescribeBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.describeBigdataBackupHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'describeBigdataBackupHost', body)

    def testModifyBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'host_name': '',
            'host_uuid': '',
            'random_str': '',
            'address': '',
            'cc_ip_uuid': '',
            'os_user': '',
            'os_pwd': '',
            'db_type': 1,
            'db_address': '',
            'db_user': '',
            'db_pwd': '',
            'dto_switch': 1,
            'dto_address': '',
            'cls_switch': 1,
            'follower_address': '',
            'bind_lic_list': '',
            'username': 'user',
            'biz_grp_list': '',
            'can_del': 1,
            'can_up': 1,
            'can_op': 1,
            'is_biz_admin': '0',
            'status': '',
            'state': {
            'host_uuid': '62D0DAD4-8B60-9627-824D-A217F8489B89',
            'status': 'ONLINE',
            'time': '1692690022',},
            'db_name': '',
            'db_port': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.modifyBigdataBackupHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'modifyBigdataBackupHost', body)

    def testDeleteBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'force': 1,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.deleteBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'deleteBigdataBackupHost', body)

    def testListBigdataBackupHoststatus(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'force_refresh': 1,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listBigdataBackupHoststatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listBigdataBackupHoststatus', body)

    def testCreateBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'platform_name': '',
            'host_uuid': '',
            'hdfs_ha': 1,
            'hdfs_config_path': '',
            'hdfs_default_fs': '',
            'hdfs_kerberos': 1,
            'hdfs_krb5_conf_path': '',
            'hdfs_keytab_path': '',
            'hdfs_principal': '',
            'hdfs_snapshot': 1,
            'hive_settings': {
            'hive_switch': 1,
            'hive_ha': 1,
            'hive_address': '',
            'hive_port': '',
            'hive_kerberos': 1,
            'hive_krb5_conf_path': '',
            'hive_keytab_path': '',
            'hive_principal': '',
            'hive_username': '',
            'hive_password': '',
            'hive_config_path': '',},
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.createBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'createBigdataPlatform', body)

    def testDescribeBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.describeBigdataPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'describeBigdataPlatform', body)

    def testModifyBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'platform_name': '',
            'platform_uuid': '',
            'host_uuid': '',
            'hdfs_ha': 1,
            'hdfs_config_path': '',
            'hdfs_default_fs': '',
            'hdfs_kerberos': 1,
            'hdfs_krb5_conf_path': '',
            'hdfs_keytab_path': '',
            'hdfs_principal': '',
            'hdfs_snapshot': 1,
            'hive_settings': {
            'hive_switch': 1,
            'hive_ha': 1,
            'hive_address': '',
            'hive_port': '',
            'hive_kerberos': 1,
            'hive_krb5_conf_path': '',
            'hive_keytab_path': '',
            'hive_principal': '',
            'hive_username': '',
            'hive_password': '',
            'hive_config_path': '',},
            'username': 'admin',
            'biz_grp_list': '',
            'can_del': 1,
            'can_up': 1,
            'can_op': 1,
            'is_biz_admin': '0',
            'status': '',
            'state': {
            'platform_uuid': '62D0DAD4-8B60-9627-824D-A217F8489B89',
            'status': 'ONLINE',
            'time': '1692690022',},
            'create_time': '',
            'user_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.modifyBigdataPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'modifyBigdataPlatform', body)

    def testListBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listBigdataPlatform', body)

    def testDeleteBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'platform_uuids': '',
            'force': '',
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.deleteBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'deleteBigdataPlatform', body)

    def testListBigdataPlatformStatus(self):
        a = Auth(username, pwd)
        body = {
            'platform_uuids': [],
            'force_refresh': 1,
        }
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listBigdataPlatformStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listBigdataPlatformStatus', body)


if __name__ == '__main__':
    unittest.main()
