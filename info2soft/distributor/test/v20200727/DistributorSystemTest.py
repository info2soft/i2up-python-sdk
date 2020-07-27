
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import DistributorSystem
# from info2soft.distributor.v20200722.DistributorSystem import DistributorSystem
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
pwd = '12345678'
    
                
class DistributorSystemTestCase(unittest.TestCase):

    def testListSysSetting(self):
        a = Auth(username, pwd)
        body = {
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.listSysSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'listSysSetting', body)

    def testUpdateSetting(self):
        a = Auth(username, pwd)
        body = {
            'cc_ip': '192.168.72.70',
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
            'email': 'test@info2sost.com',},
            'notify_contact_chk': {
            'phone': '11111111111',
            'email': 'test@info2sost.com',
            'policy': {
            'every': 'month',
            'days': '5,6',},},
            'notify_contact_status': {
            'phone': '11111111111',
            'email': 'test@info2sost.com',
            'policy': {
            'every': 'hour',
            'gap': '4',},},
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
            'title_logo': '',},
            'dist_cycle_alarm': '',
            'cmd_params': {
            'thread_num': '',
            'begin_time': '',
            'end_time': '',
            'timeout': '',},
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'updateSetting', body)

    def testQueueList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'user_uuids': [],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.queueList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'queueList', body)

    def testQueueDelete(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.queueDelete(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'queueDelete', body)

    def testUpgradeVersion(self):
        a = Auth(username, pwd)
        body = {
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.upgradeVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'upgradeVersion', body)

    def testUpdate(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.update(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'update', body)

    def testAlarmStat(self):
        a = Auth(username, pwd)
        body = {
            'user_uuids': [],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.alarmStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'alarmStat', body)

    def testAlarmLog(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'log_level': 1,
            'user_uuids': [],
            'where_args': [],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.alarmLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'alarmLog', body)

    def testCreateUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'test2',
            'password': '11111111',
            'roles': [
            '3',],
            'active': 1,
            'email': '11@info2soft.com',
            'mobile': '12366666666',
            'comment': '',
            'full_name': '',
            'property': 1,
            'type': 1,
            'begin_date': '',
            'end_date': '',
            'product_name': '',
            'sys_name': '',
            'lab_name': '',
            'contact': '',
            'address': '',
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.createUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'createUser', body)

    def testModifyUser(self):
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
            'full_name': '',
            'property': 1,
            'type': 1,
            'begin_date': '1',
            'end_date': '1',
            'product_name': '',
            'sys_name': '',
            'lab_name': '',
            'contact': '',
            'address': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.modifyUser(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'modifyUser', body)

    def testListUser(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': '',
            'search_value': '',
            'begin_date': '',
            'end_date': '',
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.listUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'listUser', body)

    def testStatUser(self):
        a = Auth(username, pwd)
        body = {
            'start': '',
            'end': '',
            'type': '',
            'limit': 1,
            'page': 1,
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.statUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'statUser', body)

    def testSyncGateway(self):
        a = Auth(username, pwd)
        body = {
            'user_name': '',
            'passwd': '',
            'node_uuid': '',
            'gw_type': '',
            'data': [{
            'ip': '',
            'port': '',
            'desc': '',
            'node': '',},],
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.syncGateway(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'syncGateway', body)

    def testSyncAccount(self):
        a = Auth(username, pwd)
        body = {
            'user_name': '',
            'passwd': '',
            'node_uuid': '',
            'data': [{
            'code': '',
            'name': '',
            'pwd': '',
            'limit': '',
            'privilege': '',
            'type_name': '',
            'enable_file': '',
            'enable_stream': '',},],
            'enable_file': '',
            'enable_stream': '',
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.syncAccount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'syncAccount', body)

    def testSendFiles(self):
        a = Auth(username, pwd)
        body = {
            'user_name': '',
            'passwd': '',
            'group_uuid': '',
            'parent_addrs': [{
            'ip': '',
            'port': '',},],
            'version': '',
        }
        
        distributorSystem = DistributorSystem(a)
        r = distributorSystem.sendFiles(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DistributorSystem', 'sendFiles', body)


if __name__ == '__main__':
    unittest.main()
