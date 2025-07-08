
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import BatchTask
from info2soft.taskCenter.v20250630.BatchTask import BatchTask
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


class BatchTaskTestCase(unittest.TestCase):
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

    def testBatchTaskList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'type': 1,
            'like_args': {
            'xxx': '',},
        }
        
        
        batchTask = BatchTask(a)
        r = batchTask.batchTaskList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchTask', 'batchTaskList', body)

    def testBatchTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'batch_uuids': [],
        }
        
        
        batchTask = BatchTask(a)
        r = batchTask.batchTaskStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchTask', 'batchTaskStatus', body)

    def testStartBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': 1,
            'del_policy': '',
        }
        
        
        batchTask = BatchTask(a)
        r = batchTask.startBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchTask', 'startBatchTask', body)

    def testStopBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': 1,
            'del_policy': '',
        }
        
        
        batchTask = BatchTask(a)
        r = batchTask.stopBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchTask', 'stopBatchTask', body)

    def testDeleteBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': 1,
            'del_policy': '',
        }
        
        
        batchTask = BatchTask(a)
        r = batchTask.deleteBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BatchTask', 'deleteBatchTask', body)


if __name__ == '__main__':
    unittest.main()
