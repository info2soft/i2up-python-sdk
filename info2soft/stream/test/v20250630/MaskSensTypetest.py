
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import MaskSensType
from info2soft.stream.v20250630.MaskSensType import MaskSensType
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


class MaskSensTypeTestCase(unittest.TestCase):
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

    def testModifySensType(self):
        a = Auth(username, pwd)
        body = {
            'algo_name': '屏蔽姓名',
            'algo_desc': '屏蔽姓名中的名字',
            'algo_params': '[{"name":"偏移量","key":"off","value":"1","setted":1,"type":"int"},{"name":"长度","key":"len","value":"0","setted":1,"type":"int"},{"name":"屏蔽字符","key":"val","value":"*","setted":0,"type":"string"}]',
            'username': 'test',
            'user_uuid': '00000000-0000-0000-0000-000000000000',
            'id': 1,
            'type_name': '姓名',
            'description': '由姓氏与名字组成，用于识别某一个人。',
            'sort': 0,
            'create_time': '0',
            'params': '',
            'parent_id': 1,
            'default_algo': 1301,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '0',
            'setted': 2,
            'type': 'int',},{
            'name': '屏蔽字符',
            'key': 'val',
            'value': '*',
            'setted': 3,
            'type': 'string',},],
        }
        
        id = 123456
        maskSensType = MaskSensType(a)
        r = maskSensType.modifySensType(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskSensType', 'modifySensType', body)

    def testListTypes(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        maskSensType = MaskSensType(a)
        r = maskSensType.listTypes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskSensType', 'listTypes', body)

    def testDescriptSensType(self):
        a = Auth(username, pwd)
        body = {
        }
        
        id = 123456
        maskSensType = MaskSensType(a)
        r = maskSensType.descriptSensType(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskSensType', 'descriptSensType', body)


if __name__ == '__main__':
    unittest.main()
