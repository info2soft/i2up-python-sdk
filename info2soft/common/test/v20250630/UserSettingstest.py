
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import UserSettings
from info2soft.common.v20250630.UserSettings import UserSettings
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


class UserSettingsTestCase(unittest.TestCase):
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

    def testListProfile(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.listProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'listProfile', body)

    def testModifyUserPwd(self):
        a = Auth(username, pwd)
        body = {
            'password': 'Info1234',
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.modifyUserPwd(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'modifyUserPwd', body)

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
        
        
        userSettings = UserSettings(a)
        r = userSettings.modifyProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'modifyProfile', body)

    def testModifyUserNotifyAddr(self):
        a = Auth(username, pwd)
        body = {
            'notify_addr': {
            'email': '',
            'phone': '',
            'webhook': {
            'res': '7134B40B-6A5F-4AFD-95ED-78A1909EAD4B',
            'rule': '',
            'compare': '',
            'cls': '',
            'nas': '',
            'hdfs': '',
            'fsp': '',
            'fsp_move': '',
            'vp': '',
            'timing': '',
            'ha': '',
            'active': 'CDACCD8B-5E6F-4908-B74C-E9F47528E38E',
            'cdm': '',
            'cloud': '',
            'routing_inspection': '',
            'all_status': '',
            'alarm': '',
            'storage': '',
            'lic': '',
            'dto': '',
            'guard_data': '',
            'bigdata_backup': '',},},
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.modifyUserNotifyAddr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'modifyUserNotifyAddr', body)

    def testLogout(self):
        a = Auth(username, pwd)
        body = {
            'lock': 1,
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.logout(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'logout', body)

    def testDescribeTwoFactor(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.describeTwoFactor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'describeTwoFactor', body)

    def testDescribeOtp(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.describeOtp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'describeOtp', body)

    def testRenewRecoveryCode(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.renewRecoveryCode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'renewRecoveryCode', body)

    def testConfigTwoFactor(self):
        a = Auth(username, pwd)
        body = {
            'enable': 1,
            'auth_code': '',
            'name': '',
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.configTwoFactor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'configTwoFactor', body)

    def testListAk(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.listAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'listAk', body)

    def testCreateAk(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.createAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'createAk', body)

    def testModifyAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
            'status': 0,
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.modifyAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'modifyAk', body)

    def testDeleteAk(self):
        a = Auth(username, pwd)
        body = {
            'access_key': 'pytDWihn3NscXewH8UYLIZq2gE7ufGoQ',
        }
        
        
        userSettings = UserSettings(a)
        r = userSettings.deleteAk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'UserSettings', 'deleteAk', body)


if __name__ == '__main__':
    unittest.main()
