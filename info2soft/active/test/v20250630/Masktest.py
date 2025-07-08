
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Mask
from info2soft.active.v20250630.Mask import Mask
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


class MaskTestCase(unittest.TestCase):
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

    def testListTypes(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        mask = Mask(a)
        r = mask.listTypes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listTypes', body)

    def testListSummaryView(self):
        a = Auth(username, pwd)
        body = {
            'src': '',
            'dst': '',
            'status': '',
            'type': '',
            'ip': '',
        }
        
        
        mask = Mask(a)
        r = mask.listSummaryView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSummaryView', body)

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
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.modifySensType(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifySensType', body)

    def testDescriptSensType(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.descriptSensType(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptSensType', body)

    def testCreateAlgo(self):
        a = Auth(username, pwd)
        body = {
            'ava_sens_type': 1,
            'parent_id': 1,
            'algo_name': '',
            'description': '',
            'params': '',
            'sort': '',
        }
        
        
        mask = Mask(a)
        r = mask.createAlgo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createAlgo', body)

    def testListAlgos(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        mask = Mask(a)
        r = mask.listAlgos(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listAlgos', body)

    def testDescriptAlgo(self):
        a = Auth(username, pwd)
        body = {
        }
        
        id = 123456
        mask = Mask(a)
        r = mask.descriptAlgo(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptAlgo', body)

    def testListMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 0,
        }
        
        
        mask = Mask(a)
        r = mask.listMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMaskRules', body)

    def testCreateMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '1231',
            'node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'tgt_db_uuid': '32C50055-A267-1E9E-65EE-FC6AAB75D390',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'other_settings': {
            'src_type': 'oracle',
            'tgt_type': 'oracle',
            'src_path': '/var/i2data/cache/',
            'file_names': [],
            'size': 1024,
            'tgt_path': '/var/i2data/cache/',
            'compress_level': 0,
            'policy': {
            'policy_type': 'immediate',
            'one_time': '',
            'time_policy': '',},
            'etl_settings': {
            'etl_table': [{
            'table': '',
            'user': '',
            'addInfo': '',
            'oprType': '',
            'process': '',},],},
            'can_approve': 0,},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': [],
            'table_space_name': [],},
            'full_sync_obj_filter': [
            'INDEX',
            'VIEW',
            'FUNCTION',
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'SYNONYM',
            'TRIGGER',
            'SEQUENCE',
            'JAVA CLASS',
            'TYPE',
            'TYPE BODY',
            'MATERIALIZED VIEW',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],
            'db_user_map': '',
            'table_map': '',
            'map_type': 'db',
            'full_sync_settings': {
            'his_thread': 1,},
            'db_map_uuid': '71D59BCE-17F3-ED0D-BC76-132833F72498',
            'strate': '',
            'modify': False,
            'bw_settings': {
            'bw_limit': '',},
        }
        
        
        mask = Mask(a)
        r = mask.createMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createMaskRules', body)

    def testStartMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        mask = Mask(a)
        r = mask.startMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'startMaskRule', body)

    def testStopMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        mask = Mask(a)
        r = mask.stopMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'stopMaskRule', body)

    def testDeleteMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        mask = Mask(a)
        r = mask.deleteMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteMaskRule', body)

    def testDescribeMaskRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.describeMaskRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'describeMaskRule', body)

    def testListMaskRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        mask = Mask(a)
        r = mask.listMaskRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMaskRuleStatus', body)

    def testDescriptMap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.descriptMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptMap', body)

    def testListMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        mask = Mask(a)
        r = mask.listMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMap', body)

    def testCreateMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
            'src_type': '',
            'src_path': '',
        }
        
        
        mask = Mask(a)
        r = mask.createMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createMap', body)

    def testModifyMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
            'src_type': '',
            'src_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.modifyMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifyMap', body)

    def testDeleteMap(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        mask = Mask(a)
        r = mask.deleteMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteMap', body)

    def testCreateDbMap(self):
        a = Auth(username, pwd)
        body = {
            'map_uuid': '',
            'map_name': 'test',
            'db_uuid': '40E3E340-8C1B-40DD-B86B-273D58C30037',
            'type_algo_map': [{
            'type_name': 'test',
            'id': 1002,
            'algo_name': 'test的基础算法',
            'default_algo': 10004,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': 'test的基础算法',},{
            'type_name': '姓名',
            'id': 1003,
            'algo_name': '屏蔽姓名',
            'default_algo': 10005,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽姓名中的名字',},{
            'type_name': '身份证号',
            'id': 1004,
            'algo_name': '屏蔽身份证出生月日',
            'default_algo': 10006,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽身份证号码中的出生月日（区间[11,14]）',},{
            'type_name': '手机号码',
            'id': 1005,
            'algo_name': '屏蔽手机号码',
            'default_algo': 10007,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽手机号码中的地区编码（区间[4,7]）',},{
            'type_name': '地址',
            'id': 1006,
            'algo_name': '屏蔽地址关键信息',
            'default_algo': 10008,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽关键信息，只保留省市信息和“区县镇路街道弄幢号楼栋单元室”等关键字',},{
            'type_name': '银行卡号',
            'id': 1007,
            'algo_name': '屏蔽银行卡号',
            'default_algo': 10009,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽银行卡号中前四位和后四位外的其它位（区间[4,-4]）',},{
            'type_name': '电子邮箱',
            'id': 1008,
            'algo_name': '屏蔽邮箱用户名',
            'default_algo': 10010,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽邮箱用户名，保留邮箱域名',},{
            'type_name': '组织机构名称',
            'id': 1009,
            'algo_name': '屏蔽组织机构名称关键信息',
            'default_algo': 10011,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽关键信息，只保留“公司所局厅部院”等关键字',},{
            'type_name': '组织机构代码',
            'id': 1010,
            'algo_name': '屏蔽组织机构代码',
            'default_algo': 10012,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽组织机构代码（区间[3,7]）',},{
            'type_name': '营业执照号码',
            'id': 1011,
            'algo_name': '屏蔽营业执照号码',
            'default_algo': 10013,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽营业执照号码中的顺序码（区间[7,14]）',},{
            'type_name': '统一社会信用代码',
            'id': 1012,
            'algo_name': '屏蔽统一社会信用代码',
            'default_algo': 10014,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽统一社会信用代码中的主体标识码（区间[9,17]）',},{
            'type_name': '中国护照号码',
            'id': 1013,
            'algo_name': '屏蔽中国护照号码',
            'default_algo': 10015,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽中国护照号码中间三位字符（区间[3,5]）',},{
            'type_name': '固定电话号码',
            'id': 1014,
            'algo_name': '屏蔽固定电话号码',
            'default_algo': 10016,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽固定电话号码中其中三位（区间[-5,-2]）',},{
            'type_name': '港澳来往内地通行证',
            'id': 1015,
            'algo_name': '屏蔽港澳居民来往内地通行证',
            'default_algo': 10017,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽港澳居民来往内地通行证号码（区间[4,7]）',},{
            'type_name': '往来港澳通行证',
            'id': 1016,
            'algo_name': '屏蔽往来港澳通行证',
            'default_algo': 10018,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽往来港澳通行证号码（区间[4,7]）',},{
            'type_name': 'IPv4地址',
            'id': 1017,
            'algo_name': '屏蔽IPv4地址',
            'default_algo': 10019,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '屏蔽IPv4地址的点分十进制后两段',},{
            'type_name': '日期',
            'id': 1018,
            'algo_name': '保留日期类型的年份',
            'default_algo': 10020,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '保留日期类型的年份不变',},{
            'type_name': '日期字符串',
            'id': 1019,
            'algo_name': '保留日期字符串的年份',
            'default_algo': 10021,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '保留日期字符串的年份不变',},{
            'type_name': '通用字符串',
            'id': 1020,
            'algo_name': '区间删除',
            'default_algo': 10022,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '删除指定区间的字符，其余部分保留',},{
            'type_name': '数值',
            'id': 1021,
            'algo_name': '',
            'default_algo': 10023,
            'default_algo_params': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 1,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '2',
            'setted': 1,
            'type': 'int',},{
            'name': '指定字符串',
            'key': 'val',
            'value': '3',
            'setted': 1,
            'type': 'string',},],
            'algo_desc': '',},],
            'sens_check_id': 'F1CAC820-4C54-40CB-B30D-94194F7B9E35',
            'src_type': 'kingbase',
            'src_path': '/var/iadata/cache/',
            'delimiter': '',
        }
        
        
        mask = Mask(a)
        r = mask.createDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createDbMap', body)

    def testListDbMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        mask = Mask(a)
        r = mask.listDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listDbMap', body)

    def testDeleteDbMap(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        mask = Mask(a)
        r = mask.deleteDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteDbMap', body)

    def testModifyDbMap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.modifyDbMap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifyDbMap', body)

    def testCreateSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'rule_name': 'adsas',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'mask_node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'user': '',
            'tabs': '',
            'row': 100,
            'min': 90,
            'sens_types': '1,2,3,4,5,6,7,8,9,10,12,13,14,15,20',
            'map_type': 'db',
            'mix': 0,
            'white': 1,
            'src_type': '',
            'src_path': '',
            'delimiter': '',
            'check_lines': 1,
        }
        
        
        mask = Mask(a)
        r = mask.createSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createSensCheck', body)

    def testModifySensCheck(self):
        a = Auth(username, pwd)
        body = {
            'username': 'admin',
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
            'rule_uuid': 'F895D958-F435-47AC-664D-805BA7DFEE89',
            'rule_name': 'asd',
            'map_type': 'db',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'user': '',
            'tabs': '',
            'row': 100,
            'min': 90,
            'sens_types': '1,2,3,4,5,6,7,8,9,10,12,13,14,15,20',
            'create_time': '1601344305',
            'mask_node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'mix': 0,
            'status': 0,
            'start': '2020-09-29 09:51:45',
            'end': '',
            'white': 1,
            'info': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.modifySensCheck(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifySensCheck', body)

    def testDeleteSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        mask = Mask(a)
        r = mask.deleteSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteSensCheck', body)

    def testListSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        
        
        mask = Mask(a)
        r = mask.listSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSensCheck', body)

    def testDescriptSensCheck(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.descriptSensCheck(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptSensCheck', body)

    def testListSensCheckStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        mask = Mask(a)
        r = mask.listSensCheckStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSensCheckStatus', body)

    def testListSensCheckResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': '',
            'user': '',
            'table': '',
            'limit': 1,
            'page': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.listSensCheckResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSensCheckResult', body)

    def testListSensCheckIgnoreCol(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'col': '',
        }
        
        
        mask = Mask(a)
        r = mask.listSensCheckIgnoreCol(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSensCheckIgnoreCol', body)

    def testListSummary(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        mask = Mask(a)
        r = mask.listSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSummary', body)

    def testAlgoTest(self):
        a = Auth(username, pwd)
        body = {
            'example': {
            'orig': '1231',
            'mask': '-',},
            'parent_id': 308,
            'ava_sens_type': 8,
            'type_arg': '',
            'id': 308,
            'params': [],
        }
        
        
        mask = Mask(a)
        r = mask.algoTest(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'algoTest', body)

    def testModifyMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'username': 'admin',
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
            'rule_uuid': 'BFD56508-9FCB-1FFF-749B-FCA2E78B4CD6',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'tgt_db_uuid': '32C50055-A267-1E9E-65EE-FC6AAB75D390',
            'rule_type': 1,
            'rule_name': '123123',
            'node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'tgt_type': 'oracle',
            'db_user_map': '',
            'row_map_mode': '',
            'map_type': 'db',
            'table_map': '',
            'dbmap_topic': '',
            'sync_mode': '1',
            'start_scn': '',
            'storage_settings': [],
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': [],
            'table_space_name': [],},
            'other_settings': {
            'src_type': 'oracle',
            'tgt_type': 'oracle',
            'src_path': '/var/i2data/cache/',
            'file_names': [],
            'size': 1024,
            'tgt_path': '/var/i2data/cache/',
            'compress_level': 0,
            'policy': {
            'policy_type': 'immediate',
            'one_time': '',
            'time_policy': '',},},
            'error_handling': [],
            'bw_settings': [],
            'strate': [{
            'type_id': 1,
            'type_arg': '',
            'algo_pid': 4,
            'algo_id': 1301,
            'sens_column': [{
            'user': '123',
            'table': '123',
            'column': '123',},],
            'algo_arg': [{
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
            'sens_map_id': '1',
            'algo_name': '屏蔽姓名',
            'sens_type_name': '姓名',},{
            'type_id': 2,
            'type_arg': '',
            'algo_pid': 4,
            'algo_id': 1302,
            'sens_column': [{
            'user': '123',
            'table': '123',
            'column': '123',},],
            'algo_arg': [{
            'name': '偏移量',
            'key': 'off',
            'value': '1',
            'setted': 4,
            'type': 'int',},{
            'name': '长度',
            'key': 'len',
            'value': '0',
            'setted': 5,
            'type': 'int',},{
            'name': '屏蔽字符',
            'key': 'val',
            'value': '*',
            'setted': 6,
            'type': 'string',},],
            'sens_map_id': '2',
            'algo_name': '屏蔽身份证出生月日',
            'sens_type_name': '身份证号',},],
            'full_sync_settings': {
            'his_thread': 1,},
            'full_sync_obj_filter': [
            'INDEX',
            'VIEW',
            'FUNCTION',
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'SYNONYM',
            'TRIGGER',
            'SEQUENCE',
            'JAVA CLASS',
            'TYPE',
            'TYPE BODY',
            'MATERIALIZED VIEW',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],
            'inc_sync_ddl_filter': '',
            'filter_table_settings': '',
            'etl_settings': '',
            'create_time': 1601345043,
            'start_rule_now': 1,
            'db_map_uuid': '71D59BCE-17F3-ED0D-BC76-132833F72498',
            'dml_track': '',
            'kafka_time_out': '12000',
            'part_load_balance': 'by_key',
            'kafka_message_encoding': 'UTF-8',
            'kafka': '',
            'biz_grp_list': [],
            'biz_grp_name': [],
            'modify': True,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.modifyMaskRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifyMaskRules', body)

    def testCreateApprove(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '67Bf70F4-Fef7-9E74-4BBa-8D1BdDa02CFD',
        }
        
        
        mask = Mask(a)
        r = mask.createApprove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createApprove', body)

    def testImportMaskRuleInfo(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mask = Mask(a)
        r = mask.importMaskRuleInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'importMaskRuleInfo', body)


if __name__ == '__main__':
    unittest.main()
