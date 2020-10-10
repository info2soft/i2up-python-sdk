# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.Settings import Settings
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


class UserTestCase(unittest.TestCase):
    
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
                'email': 'test@info2sost.com',
            },
            'notify_contact_chk': {
                'phone': '11111111111',
                'email': 'test@info2sost.com',
                'policy': {
                    'every': '1',
                    'days': '5'
                },
            },
            'notify_contact_status': {
                'phone': '11111111111',
                'email': 'test@info2sost.com',
                'policy': {
                    'every': '3',
                    'gap': '4'
                },
            },
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
        }
        setter = Settings(a)
        r = setter.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'updateSetting', body)

    def testListSysSetting(self):
        a = Auth(username, pwd)
        body = {
            'keys': [],
        }
        setter = Settings(a)
        r = setter.listSysSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listSysSetting', body)

    def testDescribeCCip(self):
        a = Auth(username, pwd)
        body = {}
        setter = Settings(a)
        r = setter.describeCCip()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeCCip', body)

    def testListPublicSettings(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.listPublicSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listPublicSettings', body)

    def testDescribe(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.describe(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describe', body)

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

        system = Settings(a)
        r = system.createUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createUser', body)

    def testListUser(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
        }

        system = Settings(a)
        r = system.listUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listUser', body)

    def testDescribeUser(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        system = Settings(a)
        r = system.describeUser(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'describeUser', body)

    def testDeleteUser(self):
        a = Auth(username, pwd)
        body = {
            'ids': [
            '20',],
        }

        system = Settings(a)
        r = system.deleteUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'deleteUser', body)

    def testModifyUser(self):
        a = Auth(username, pwd)
        body = {
            'username': 'admin',
            'password': '11111111',
            'roles': [
                '3',
            ],
            'active': '1',
            'email': '123@info2soft.com',
            'mobile': '12332145248',
            'comment': '',
            'first_name': '',
            'last_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        system = Settings(a)
        r = system.modifyUser(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUser', body)

    def testModifyUserPwd(self):
        a = Auth(username, pwd)
        body = {
            'old_password': 'Info1234',
            'password': 'Info1234',
        }

        system = Settings(a)
        r = system.modifyUserPwd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyUserPwd', body)

    def testListProfile(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.listProfile(body)
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

        system = Settings(a)
        r = system.modifyProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyProfile', body)

    def testLogout(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.logout(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'logout', body)

    def testListAk(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.listAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listAk', body)

    def testCreateAk(self):
        a = Auth(username, pwd)
        body = {
        }

        system = Settings(a)
        r = system.createAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'createAk', body)

    def testModifyAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
            'status': 0,
        }

        system = Settings(a)
        r = system.modifyAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'modifyAk', body)

    def testDeleteAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
        }

        system = Settings(a)
        r = system.deleteAk(body)
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

        system = Settings(a)
        r = system.listRole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Settings', 'listRole', body)


if __name__ == '__main__':
    unittest.main()  
