
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import FindPassword
from info2soft.common.v20250630.FindPassword import FindPassword
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


class FindPasswordTestCase(unittest.TestCase):
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

    def testIsAccountExists(self):
        a = Auth(username, pwd)
        body = {
            'account': '',
            'type': 'email ',
        }
        
        
        findPassword = FindPassword(a)
        r = findPassword.isAccountExists(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FindPassword', 'isAccountExists', body)

    def testSendVerificationCode(self):
        a = Auth(username, pwd)
        body = {
            'account': '',
            'type': 'mobile',
        }
        
        
        findPassword = FindPassword(a)
        r = findPassword.sendVerificationCode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FindPassword', 'sendVerificationCode', body)

    def testVerifyVerficationCode(self):
        a = Auth(username, pwd)
        body = {
            'account': '',
            'verification_code': '',
            'type': 'mobile',
        }
        
        
        findPassword = FindPassword(a)
        r = findPassword.verifyVerficationCode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FindPassword', 'verifyVerficationCode', body)

    def testResetPassword(self):
        a = Auth(username, pwd)
        body = {
            'account': '',
            'password': '',
            'type': '',
            'verification_code': '',
        }
        
        
        findPassword = FindPassword(a)
        r = findPassword.resetPassword(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FindPassword', 'resetPassword', body)


if __name__ == '__main__':
    unittest.main()
