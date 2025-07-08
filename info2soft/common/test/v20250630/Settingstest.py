
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Settings
from info2soft.common.v20250630.Settings import Settings
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


class SettingsTestCase(unittest.TestCase):
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

    def testListSysSetting(self):
        a = Auth(username, pwd)
        body = {
            'keys': [],
        }
        
        
        settings = Settings(a)
        r = settings.listSysSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listSysSetting', body)

    def testUpdateSetting(self):
        a = Auth(username, pwd)
        body = {
            'cc_ips': [],
            'log_save_time': '30',
            'page_size': '10',
            'refresh_interval': '10',
            'email_smtp_svr': 'test',
            'email_smtp_port': '25',
            'email_smtp_ssl': '0',
            'email_smtp_auth': '1',
            'email_account': 'test@info2soft.com',
            'email_pwd': '123456',
            'email_switch': '1',
            'sms_switch': '1',
            'sms_platform': 'ali',
            'sms_app_key': 'AppKey',
            'sms_secret_key': 'SecretKey',
            'sms_sign_name': 'SignName',
            'sms_template_code': 'template',
            'sms_server': '',
            'sms_username': '',
            'sms_password': '',
            'sms_domain_name': '',
            'sms_region_name': '',
            'sms_topic_urn': '',
            'node_latest_ver': '',
            'node_upgrade_server': '',
            'node_upgrade_path': '',
            'node_online_upgrade': '0',
            'mirr_skip': '0',
            'passwd_expire': '30',
            'passwd_length': '8',
            'passwd_strong': '1',
            'login_attempt': '13',
            'login_lock': '10',
            'client_lang': 'zh_cn',
            'offline_mode': 0,
            'dtu_serial_device': '',
            'dtu_baud_rate': '',
            'email_title': '',
            'email_content': '',
            'email_from': '',
            'product_title': {
            'title': '',
            'copyright': '',
            'favicon': '',
            'copyright_logo': '',
            'login_background': '',
            'login_logo': '',
            'home_logo': '',
            'home_background': '',
            'title_logo': '',},
            'ylj_channel_no': '0001',
            'ylj_system_no': '0001',
            'log_path': '',
            'max_log_path_size': 1,
            'log_archive_path': '',
            'max_disk_occupancy': 0,
            'app_id': '',
            'app_secret': '',
            'wechat_switch': 0,
            'wechat_token': '',
            'aes_key': '',
            'maintenance_switch': 0,
            'maintenance_source_id': '',
            'maintenance_default_ip': '',
            'maintenance_user_id': '',
            'maintenance_ip': '',
            'white_list': '[0.0.0.0]',
            'etcd_urls': [{
            'urls': [{
            'ip': '',
            'etcd_port': '',
            'rpc_port': '',
            'data_port': '',},],
            'uuid': '',
            'has_node': 1,
            'name': '',},],
            'maintenance_platform': '',
            'maintenance_username': '',
            'maintenance_password': '',
            'maintenance_source_system_code': '',
            'maintenance_source_system_name': '',
            'maintenance_event_system_code': '',
            'maintenance_event_system_name': '',
            'snmp_switch': 0,
            'snmp_version': '',
            'snmp_community': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'maintenance_apikey': '',
            'maintenance_app_key': '',
            'maintenance_alarm_name': '',
            'rc_protection': 0,
            'public_key_expire': 1,
            'weak_pwd_dic': [],
            'backup_work_limit': 7,
            'file_certification': 1,
            'cfs_mount_path': '',
            'rule_version_limit': 1,
            'dto_archive_switch': '',
            'dto_archive_db_addr': '',
            'dto_archive_db_port': '',
            'dto_archive_db_user': '',
            'dto_archive_db_pass': '',
            'dto_archive_db_name': '',
            'login_method_switch': 1,
            'email_login': 1,
            'sms_login': 1,
            'ldap_login': '',
            'sms_app_id': '',
            'sms_sign_key': '',
            'sms_encrypt_key': '',
            'lic_quota_switch': 1,
            'kernel_upgrade_switch': '',
            'kernel_upgrade_server': '',
            'kernel_upgrade_path': '',
        }
        
        
        settings = Settings(a)
        r = settings.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateSetting', body)

    def testUpdateSecuritySetting(self):
        a = Auth(username, pwd)
        body = {
            'white_list': '[0.0.0.0]',
            'weak_pwd_dic': [],
            'public_key_expire': 1,
            'passwd_expire': '30',
            'passwd_length': '8',
            'passwd_strong': '1',
            'login_attempt': '13',
            'login_lock': '10',
            'login_limit': '1',
            'cert_alarm_threshold': '30',
        }
        
        
        settings = Settings(a)
        r = settings.updateSecuritySetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateSecuritySetting', body)

    def testDescribeCCip(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.describeCCip(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeCCip', body)

    def testListPublicSettings(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.listPublicSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listPublicSettings', body)

    def testUpdateNotifySetting(self):
        a = Auth(username, pwd)
        body = {
            'app_id': '',
            'app_secret': '',
            'maintenance_platform': '',
            'maintenance_username': '',
            'maintenance_password': '',
            'maintenance_source_system_code': '',
            'maintenance_source_system_name': '',
            'maintenance_event_system_code': '',
            'maintenance_apikey': '',
            'maintenance_app_key': '',
            'file_certification': 1,
            'wechat_switch': 0,
            'wechat_token': '',
            'maintenance_switch': 0,
            'maintenance_source_id': '',
            'etcd_urls': [{
            'urls': [{
            'ip': '',
            'etcd_port': '',
            'rpc_port': '',
            'data_port': '',},],
            'uuid': '',
            'has_node': 1,
            'name': '',},],
            'maintenance_default_ip': '',
            'maintenance_user_id': '',
            'email_smtp_svr': 'test',
            'email_smtp_port': '25',
            'email_smtp_ssl': '0',
            'email_smtp_auth': '1',
            'email_account': 'test@info2soft.com',
            'email_pwd': '123456',
            'email_switch': '1',
            'sms_switch': '1',
            'sms_platform': 'ali',
            'dtu_serial_device': '',
            'sms_app_key': 'AppKey',
            'dtu_baud_rate': '',
            'aes_key': '',
            'sms_secret_key': 'SecretKey',
            'sms_sign_name': 'SignName',
            'sms_template_code': 'template',
            'sms_server': '',
            'sms_username': '',
            'sms_password': '',
            'sms_domain_name': '',
            'maintenance_event_system_name': '',
            'sms_region_name': '',
            'sms_topic_urn': '',
            'snmp_switch': 0,
            'snmp_version': '',
            'snmp_community': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'maintenance_alarm_name': '',
            'email_title': '',
            'email_content': '',
            'maintenance_ip': '',
            'sms_app_id': '',
            'sms_sign_key': '',
            'sms_encrypt_key': '',
            'ylj_channel_no': '0001',
            'ylj_system_no': '0001',
            'email_from': '',
        }
        
        
        settings = Settings(a)
        r = settings.updateNotifySetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateNotifySetting', body)

    def testUpdateNodeConf(self):
        a = Auth(username, pwd)
        body = {
            'node_conf': {
            'windows': {
            'log_path': '/var/i2data/log/',
            'keep_log_days': 180,
            'log_limit': 1024,
            'cache_path': '/var/i2data/cache/',
            'mem_limit_percent': 100,
            'disk_limit': 10240,
            'mon_send_interval': 10,
            'mon_data_path': '/var/i2data/log/',
            'db_save_day': 3,
            'mon_save_day': 5,
            'bak_meta_data_path': '/var/i2data/meta_data/',
            'temp_path': '',
            'disk_free_space_limit': 1,
            'bak_cache_data_dir': '',
            'bak_cache_data_upper_limit': 1,
            'bak_cache_disk_lower_limit': 1,
            'log_interval': 60,
            'rw_server_port': 1,},
            'linux': {
            'keep_log_days': 1,
            'log_path': '',
            'log_limit': 1,
            'cache_path': '',
            'mem_limit_percent': 1,
            'disk_limit': 1,
            'mon_send_interval': 1,
            'mon_data_path': '',
            'db_save_day': 1,
            'mon_save_day': 1,
            'bak_meta_data_path': '',
            'temp_path': '',
            'disk_free_space_limit': 1,
            'bak_cache_data_dir': '',
            'bak_cache_data_upper_limit': 1,
            'bak_cache_disk_lower_limit': 1,
            'log_interval': 60,
            'rw_server_port': 1,},
            'roles_info': {
            'role': 1,
            'modules': [],
            'processes': [],},
            'roles': [
            '1',
            '2',
            '4',
            '8',],},
        }
        
        
        settings = Settings(a)
        r = settings.updateNodeConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateNodeConf', body)

    def testListNodeConf(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.listNodeConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listNodeConf', body)

    def testCreateUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'test2',
            'password': '11111111',
            'roles': [
            '3',],
            'active': '1',
            'email': '11@info2soft.com',
            'mobile': '12366666666',
            'comment': '',
        }
        
        
        settings = Settings(a)
        r = settings.createUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createUser', body)

    def testListUser(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
        }
        
        
        settings = Settings(a)
        r = settings.listUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listUser', body)

    def testDescribeUser(self):
        a = Auth(username, pwd)
        body = {
        }
        
        id = 123456
        settings = Settings(a)
        r = settings.describeUser(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeUser', body)

    def testDeleteUser(self):
        a = Auth(username, pwd)
        body = {
            'ids': [
            '20',],
        }
        
        
        settings = Settings(a)
        r = settings.deleteUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteUser', body)

    def testClearLoginAttempt(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        settings = Settings(a)
        r = settings.clearLoginAttempt(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'clearLoginAttempt', body)

    def testModifyUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'test',
            'password': '11111111',
            'roles': [
            '3',],
            'active': '1',
            'email': '123@info2soft.com',
            'mobile': '12332145248',
            'comment': '',
            'first_name': '',
            'last_name': '',
        }
        
        id = 123456
        settings = Settings(a)
        r = settings.modifyUser(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUser', body)

    def testModifyUserEmailOrMobile(self):
        a = Auth(username, pwd)
        body = {
            'user_uuid': '',
            'mobile': '',
            'email': '',
        }
        
        
        settings = Settings(a)
        r = settings.modifyUserEmailOrMobile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUserEmailOrMobile', body)

    def testListRole(self):
        a = Auth(username, pwd)
        body = {
            'filter_value': 'operator',
            'filter_type': 'name',
            'page': '1',
            'limit': '10',
        }
        
        
        settings = Settings(a)
        r = settings.listRole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listRole', body)

    def testListNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        
        settings = Settings(a)
        r = settings.listNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listNpsvr', body)

    def testDescribeNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '9C865EB7-6999-65D6-C029-0615735C137E',
        }
        
        
        settings = Settings(a)
        r = settings.describeNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeNpsvr', body)

    def testModifyNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '9C865EB7-6999-65D6-C029-0615735C137E',
            'bkup_switch': '0',
            'policy': {
            'limit': '30',
            'bkup_type': '0',
            'time': '24',},
            'random_str': '9C865EB7-6999-65D6-C029-0615735C137E',
        }
        
        
        settings = Settings(a)
        r = settings.modifyNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyNpsvr', body)

    def testDeleteNpsvr(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '',
        }
        
        
        settings = Settings(a)
        r = settings.deleteNpsvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteNpsvr', body)

    def testListNpsvrStatus(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuids': '',
        }
        
        
        settings = Settings(a)
        r = settings.listNpsvrStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listNpsvrStatus', body)

    def testListNpsvrBakList(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '',
        }
        
        
        settings = Settings(a)
        r = settings.listNpsvrBakList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listNpsvrBakList', body)

    def testRecoveryNpsvrBak(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'operate': '',
        }
        
        
        settings = Settings(a)
        r = settings.recoveryNpsvrBak(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'recoveryNpsvrBak', body)

    def testDeleteNpsvrBak(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'operate': '',
        }
        
        
        settings = Settings(a)
        r = settings.deleteNpsvrBak(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteNpsvrBak', body)

    def testListBakConfig(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'obj_type': 'dto',
        }
        
        
        settings = Settings(a)
        r = settings.listBakConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listBakConfig', body)

    def testDescribeBakConfig(self):
        a = Auth(username, pwd)
        body = {
            'obj_uuid': '',
        }
        
        
        settings = Settings(a)
        r = settings.describeBakConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeBakConfig', body)

    def testModifyBakConfig(self):
        a = Auth(username, pwd)
        body = {
            'obj_uuid': '9C865EB7-6999-65D6-C029-0615735C137E',
            'bkup_switch': '0',
            'policy': {
            'limit': 30,
            'bkup_type': 0,
            'time': 24,},
            'random_str': '9C865EB7-6999-65D6-C029-0615735C137E',
        }
        
        
        settings = Settings(a)
        r = settings.modifyBakConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyBakConfig', body)

    def testDeleteBakConfig(self):
        a = Auth(username, pwd)
        body = {
            'obj_uuid': '',
        }
        
        
        settings = Settings(a)
        r = settings.deleteBakConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteBakConfig', body)

    def testListBakConfigStatus(self):
        a = Auth(username, pwd)
        body = {
            'obj_uuids': [],
        }
        
        
        settings = Settings(a)
        r = settings.listBakConfigStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listBakConfigStatus', body)

    def testListBakHistory(self):
        a = Auth(username, pwd)
        body = {
            'obj_uuid': '',
        }
        
        
        settings = Settings(a)
        r = settings.listBakHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listBakHistory', body)

    def testImportConfig(self):
        a = Auth(username, pwd)
        body = {
            'keep_cc_ip': 1,
        }
        
        
        settings = Settings(a)
        r = settings.importConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'importConfig', body)

    def testExportConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.exportConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'exportConfig', body)

    def testRecoveryBakConfigInfo(self):
        a = Auth(username, pwd)
        body = {
            'id': 1,
            'operate': '',
        }
        
        
        settings = Settings(a)
        r = settings.recoveryBakConfigInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'recoveryBakConfigInfo', body)

    def testDeleteBakConfigInfo(self):
        a = Auth(username, pwd)
        body = {
            'id': 1,
            'operate': '',
        }
        
        
        settings = Settings(a)
        r = settings.deleteBakConfigInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteBakConfigInfo', body)

    def testDescribeCtrlBakSetting(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.describeCtrlBakSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeCtrlBakSetting', body)

    def testModifyCtrlBakSetting(self):
        a = Auth(username, pwd)
        body = {
            'bak_type': 0,
            'bak_path': '',
            'auto_switch': 1,
            'bak_policy': {
            'policy': '',
            'hour': '',},
            'bak_limit': 1,
            'storage_type': '',
            'remote_settings': {
            'host': '',
            'username': '',
            'password': '',
            'port': 21,
            'ssl': True,
            'passive': True,
            'timeout': 60,
            'root': '',
            'private_key': '',},
        }
        
        
        settings = Settings(a)
        r = settings.modifyCtrlBakSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyCtrlBakSetting', body)

    def testListDownloadCustomAudio(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.listDownloadCustomAudio(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listDownloadCustomAudio', body)

    def testUploadDownloadCustomAudio(self):
        a = Auth(username, pwd)
        body = {
            'custom_audio': {},
        }
        
        
        settings = Settings(a)
        r = settings.uploadDownloadCustomAudio(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'uploadDownloadCustomAudio', body)

    def testDeleteDownloadCustomAudio(self):
        a = Auth(username, pwd)
        body = {
            'custom_audio': '',
        }
        
        
        settings = Settings(a)
        r = settings.deleteDownloadCustomAudio(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteDownloadCustomAudio', body)

    def testDownloadCustomAudio(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.downloadCustomAudio(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'downloadCustomAudio', body)

    def testListErrorCode(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        settings = Settings(a)
        r = settings.listErrorCode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listErrorCode', body)


if __name__ == '__main__':
    unittest.main()
