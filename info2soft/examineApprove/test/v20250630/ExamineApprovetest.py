
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ExamineApprove
from info2soft.examineApprove.v20250630.ExamineApprove import ExamineApprove
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


class ExamineApproveTestCase(unittest.TestCase):
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

    def testCreateExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'approver_uuid': '',
            'rule_uuid': '',
            'rule_file': '',
            'confirm_email': '',
            'uuid': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.createExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'createExamineApprove', body)

    def testListExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'limit': 15,
            'page': 1,
            'search_value': '',
            'search_field': '',
            'where_args': [{
            'status': '',
            'rule_type': 1,},],
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.listExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'listExamineApprove', body)

    def testApproveExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
            'approve_result': '',
            'approve_time': '',
            'comment': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.approveExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'approveExamineApprove', body)

    def testEnableExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
            'approve_result': '',
            'approve_time': '',
            'comment': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.enableExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'enableExamineApprove', body)

    def testReceiptExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
            'approve_result': '',
            'approve_time': '',
            'comment': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.receiptExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'receiptExamineApprove', body)

    def testDeleteExamineApprove(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
            'approve_result': '',
            'approve_time': '',
            'comment': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.deleteExamineApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'deleteExamineApprove', body)

    def testListExamineApproveApproverList(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.listExamineApproveApproverList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'listExamineApproveApproverList', body)

    def testExamineApproveImport(self):
        a = Auth(username, pwd)
        body = {
            'examine_approve_file': '',
            'uuid': '',
            'name': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.examineApproveImport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'examineApproveImport', body)

    def testListExamineApproveFileInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.listExamineApproveFileInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'listExamineApproveFileInfo', body)

    def testExamineApproveDownlowdFile(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'column': '',
        }
        
        
        examineApprove = ExamineApprove(a)
        r = examineApprove.examineApproveDownlowdFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ExamineApprove', 'examineApproveDownlowdFile', body)


if __name__ == '__main__':
    unittest.main()
