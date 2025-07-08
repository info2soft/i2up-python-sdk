
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ObjCmp
from info2soft.stream.v20250630.ObjCmp import ObjCmp
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


class ObjCmpTestCase(unittest.TestCase):
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

    def testCreateDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
            'db_user_map': {'src_user':'dst_user'},
            'config': {
            'one_task': 'immediate',},
            'policies': '',
            'policy_type': 'periodic',
            'one_time': '2019-05-27 16:07:08',
            'repair': 1,
            'obj_cmp_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cal_table_recoders': 1,
            'cmp_type': 'user',
            'rule_uuid': '751A03F5-C97D-645B-82B2-316A5D198528',
            'obj_cmp_type': '',
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.createDatacheckObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'createDatacheckObjCmp', body)

    def testDeleteDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': False,
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.deleteDatacheckObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'deleteDatacheckObjCmp', body)

    def testStopObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.stopObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'stopObjCmp', body)

    def testRestartObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.restartObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'restartObjCmp', body)

    def testCmpStopTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.cmpStopTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'cmpStopTimeObjCmp', body)

    def testCmpResumeTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.cmpResumeTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'cmpResumeTimeObjCmp', body)

    def testCmpImmediateObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.cmpImmediateObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'cmpImmediateObjCmp', body)

    def testExportSyncObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'include_active_db': 1,
            'include_active_node': 1,
            'rule_uuids': [],
        }
        
        
        objCmp = ObjCmp(a)
        r = objCmp.exportSyncObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ObjCmp', 'exportSyncObjCmp', body)


if __name__ == '__main__':
    unittest.main()
