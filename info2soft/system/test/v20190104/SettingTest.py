# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.system.v20181227.Settings import Settings
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


if __name__ == '__main__':
    unittest.main()  
