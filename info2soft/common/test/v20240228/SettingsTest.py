# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.Settings import Settings
# from info2soft.common.v20200722.Settings import Settings
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
            'notify_contact_biz': {
                'phone': '11111111111',
                'email': 'test@info2sost.com', },
            'notify_contact_chk': {
                'phone': '11111111111',
                'email': 'test@info2sost.com',
                'policy': {
                    'every': 'month',
                    'days': '5,6', }, },
            'notify_contact_status': {
                'phone': '11111111111',
                'email': 'test@info2sost.com',
                'policy': {
                    'every': 'hour',
                    'gap': '4', }, },
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
            'notify_limit': '10',
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
                'title_logo': '', },
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
            'normal_notify_switch': 0,
            'sms_id': '',
            'wechat_id': '',
            'maintenance_switch': 0,
            'maintenance_source_id': '',
            'maintenance_default_ip': '',
            'maintenance_user_id': '',
            'maintenance_ip': '',
            'white_list': '[0.0.0.0]',
            'stop_alerts': 1,
            'etcd_urls': [{
                'urls': [{
                    'ip': '',
                    'port': '', }, ],
                'uuid': '',
                'has_node': 1,
                'name': '', }, ],
            'audio_alert_notify': 1,
            'single_alert_loop_broadcast_times': 1,
            'custom_audio': '',
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
        }

        settings = Settings(a)
        r = settings.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateSetting', body)

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

    def testListPublicSettings(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.listPublicSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listPublicSettings', body)

    def testDescribeCCip(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.describeCCip(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeCCip', body)

    def testCreateUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'test2',
            'password': '11111111',
            'roles': [
                '3', ],
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
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        settings = Settings(a)
        r = settings.describeUser(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeUser', body)

    def testDeleteUser(self):
        a = Auth(username, pwd)
        body = {
            'ids': [
                '20', ],
        }

        settings = Settings(a)
        r = settings.deleteUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteUser', body)

    def testModifyUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'test',
            'password': '11111111'
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        settings = Settings(a)
        r = settings.modifyUser(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUser', body)

    def testModifyUserPwd(self):
        a = Auth(username, pwd)
        body = {
            'old_password': 'Info1234',
            'password': 'Info1234',
        }

        settings = Settings(a)
        r = settings.modifyUserPwd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUserPwd', body)

    def testListProfile(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.listProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listProfile', body)

    def testModifyProfile(self):
        a = Auth(username, pwd)
        body = {
            'mobile': '15354254585',
            'email': 'test@info2soft.com',
            'nickname': 'test',
            'company': 'info2soft',
            'address': 'test',
            'comment': '',
        }

        settings = Settings(a)
        r = settings.modifyProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyProfile', body)

    def testLogout(self):
        a = Auth(username, pwd)
        body = {
            'lock': 1,
        }

        settings = Settings(a)
        r = settings.logout(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'logout', body)

    def testListAk(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
        }

        settings = Settings(a)
        r = settings.listAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listAk', body)

    def testCreateAk(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
        }

        settings = Settings(a)
        r = settings.createAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createAk', body)

    def testModifyAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
            'status': 0,
        }

        settings = Settings(a)
        r = settings.modifyAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyAk', body)

    def testDeleteAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
        }

        settings = Settings(a)
        r = settings.deleteAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteAk', body)

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
                'time': '24', },
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

    def testNpsvrBakRecovery(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'operate': '',
        }

        settings = Settings(a)
        r = settings.npsvrBakRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'npsvrBakRecovery', body)

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
                'time': 24, },
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
            'obj_uuids': ["adsfasd", "asdfadsf"],
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
                'hour': '', },
            'bak_limit': 1,
            'storage_type': '',
            'remote_settings': {
                'host': '',
                'username': '',
                'password': '',
                'port': 21,
                'ssl': 1,
                'passive': 1,
                'timeout': 60,
                'root': '',
                'private_key': '', },
        }

        settings = Settings(a)
        r = settings.modifyCtrlBakSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyCtrlBakSetting', body)

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

    def testDownloadCustomAudio(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.downloadCustomAudio(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'downloadCustomAudio', body)

    def testChkEtcdUrl(self):
        a = Auth(username, pwd)
        body = {
            'etcd_url_uuid': '',
        }

        settings = Settings(a)
        r = settings.chkEtcdUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'chkEtcdUrl', body)

    def testCreateUpdateScheduleSvr(self):
        a = Auth(username, pwd)
        body = {
            'node_access_list': [{
            'ip': '',
            'uuid': '',},],
            'os_pwd': '',
            'os_user': '',
            'rpc_port': '',
            'data_port': '',
            'rpc_addr': '',
            'etcd_url_uuid': '',
            'bkset_meta_data_path': '',
            'log_dir': '',
            'log_save_time': 1,
            'log_save_size': 1,
        }

        settings = Settings(a)
        r = settings.createUpdateScheduleSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createUpdateScheduleSvr', body)

    def testListScheduleSvr(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.listScheduleSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listScheduleSvr', body)

    def testDeleteScheduleSvr(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }

        settings = Settings(a)
        r = settings.deleteScheduleSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteScheduleSvr', body)

    def testCreateUpdateEtcd(self):
        a = Auth(username, pwd)
        body = {
            'user': '',
            'pwd': '',
            'cls_conf': [{
            'ip': '',
            'port': '',},],
            'node_access_list': [{
            'name': '',
            'ip_list': [{
            'ip': '',
            'port': '',},],
            'uuid': '',},],
        }

        settings = Settings(a)
        r = settings.createUpdateEtcd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createUpdateEtcd', body)

    def testListEtcd(self):
        a = Auth(username, pwd)
        body = {
        }

        settings = Settings(a)
        r = settings.listEtcd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listEtcd', body)


if __name__ == '__main__':
    unittest.main()
