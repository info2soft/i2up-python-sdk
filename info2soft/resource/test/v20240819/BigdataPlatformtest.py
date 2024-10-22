
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BigdataPlatform
from info2soft.resource.v20240819.BigdataPlatform import BigdataPlatform
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


class BigdataPlatformTestCase(unittest.TestCase):

    def testAuthBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'os_user': '',
            'os_pwd': '',
            'address': '',
            'config_port': 1,
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.authBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'authBigdataBackupHost', body)

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
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.bigdataBackupHostDbAuth(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'bigdataBackupHostDbAuth', body)

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
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.createBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'createBigdataBackupHost', body)

    def testListBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.listBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'listBigdataBackupHost', body)

    def testDescribeBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.describeBigdataBackupHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'describeBigdataBackupHost', body)

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
            'username': 'admin',
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
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.modifyBigdataBackupHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'modifyBigdataBackupHost', body)

    def testDeleteBigdataBackupHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'force': 1,
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.deleteBigdataBackupHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'deleteBigdataBackupHost', body)

    def testListBigdataBackupHoststatus(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'force_refresh': 1,
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.listBigdataBackupHoststatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'listBigdataBackupHoststatus', body)

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
            'hive_config_path': '',},
            'hive_password': '',
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.createBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'createBigdataPlatform', body)

    def testDescribeBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.describeBigdataPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'describeBigdataPlatform', body)

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
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.modifyBigdataPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'modifyBigdataPlatform', body)

    def testListBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.listBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'listBigdataPlatform', body)

    def testDeleteBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'platform_uuids': '',
            'force': '',
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.deleteBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'deleteBigdataPlatform', body)

    def testListBigdataPlatformStatus(self):
        a = Auth(username, pwd)
        body = {
            'platform_uuids': [],
            'force_refresh': 1,
        }
        
        
        bigdataPlatform = BigdataPlatform(a)
        r = bigdataPlatform.listBigdataPlatformStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataPlatform', 'listBigdataPlatformStatus', body)


if __name__ == '__main__':
    unittest.main()
