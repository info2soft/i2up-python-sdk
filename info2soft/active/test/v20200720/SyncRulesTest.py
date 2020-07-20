
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.active.v20200720.SyncRules import SyncRules
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
    
                
class SyncRulesTestCase(unittest.TestCase):

    def testDescribeSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'BaeeC5C6-ceAD-A66b-dD5E-F05bD59Ad178',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesObjInfo', body)

    def testDescribeSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'usr': '',
            'rule_uuid': 'bFAf6DA9-6Eef-1dE3-7fF7-22E9E1ccbf7b',
            'sort_order': 'asc',
            'search': '',
            'sort': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesDML', body)

    def testDescribeSyncRulesProxyStatus(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesProxyStatus()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesProxyStatus', body)

    def testDescribeSyncRulesHasSync(self):
        a = Auth(username, pwd)
        body = {
            'offset': '0',
            'limit': 10,
            'row_uuid': 'b2528cf8-F0c9-CfFE-DDAe-dBfc3dFdFcb2',
            'search': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesHasSync(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesHasSync', body)

    def testDescribeSyncRulesFailObj(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'd9779eB3-Ee1c-F312-cc78-55f2BdFf4B5E',
            'search': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesFailObj(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesFailObj', body)

    def testCreateSyncRules(self):
        a = Auth(username, pwd)
        body = {
            "rule_name": "ctt->ctt",
            "src_db_uuid": " 1B1153F6-DAD9-BC39-888A-A743FCC208E5",
            "tgt_db_uuid": " D42BF707-C971-EEA9-521F-BB0F3F7A92FC",
            "tgt_type": "oracle",
            "db_user_map": {
                "CTT": "CTT"
            },
            "row_map_mode": "rowid",
            "map_type": "user",
            "table_map": [
                {}
            ],
            "dbmap_topic": "",
            "sync_mode": 1,
            "start_scn": 1,
            "full_sync_settings": {
                "keep_exist_table": 0,
                "keep_table": 0,
                "load_mode": "direct",
                "ld_dir_opt": 0,
                "his_thread": 1,
                "try_split_part_table": 0,
                "concurrent_table": [
                    "hello.world"
                ]
            },
            "full_sync_obj_filter": {
                "full_sync_obj_data": [
                    "PROCEDURE",
                    "PACKAGE",
                    "PACKAGE BODY",
                    "DATABASE LINK",
                    "OLD JOB",
                    "JOB",
                    "PRIVS",
                    "CONSTRAINT",
                    "JAVA RESOURCE",
                    "JAVA SOURCE"
                ]
            },
            "inc_sync_ddl_filter": {
                "inc_sync_ddl_data": [
                    "INDEX",
                    "VIEW",
                    "FUNCTION"
                ]
            },
            "filter_table_settings": {
                "exclude_table": [
                    "hh.ww"
                ]
            },
            "etl_settings": {
                "etl_table": [
                    {
                        "oprType": "IRP",
                        "table": "",
                        "user": "",
                        "process": "SKIP",
                        "addInfo": ""
                    }
                ]
            },
            "start_rule_now": 0,
            "storage_settings": {
                "src_max_mem": 512,
                "src_max_disk": 5000,
                "txn_max_mem": 10000,
                "tf_max_size": 100,
                "tgt_extern_table": ""
            },
            "error_handling": {
                "load_err_set": "continue",
                "drp": "ignore",
                "irp": "irpafterdel",
                "urp": "toirp"
            },
            "table_space_map": {
                "tgt_table_space": "",
                "table_mapping_way": "ptop",
                "table_path_map": {
                    "ddd": "sss",
                    "ddd1": "sss1"
                },
                "table_space_name": {
                    "qq": "ss"
                }
            },
            "other_settings": {
                "keep_dyn_data": 0,
                "dyn_thread": 1,
                "dly_constraint_load": 0,
                "zip_level": 0,
                "ddl_cv": 0,
                "keep_bad_act": 0,
                "keep_usr_pwd": 1,
                "convert_urp_of_key": 0,
                "ignore_foreign_key": 0
            },
            "bw_settings": {
                "bw_limit": "\"12*00:00-13:00*40M,3*00:00-13:00*40M\""
            },
            "biz_grp_list": [],
            "kafka_time_out|12000": "",
            "part_load_balance": ""
        }
        syncRules = SyncRules(a)
        r = syncRules.createSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createSyncRules', body)

    def testModifySyncRules(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.modifySyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'modifySyncRules', body)

    def testDescribeSyncRulesLoadInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesLoadInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesLoadInfo', body)

    def testDeleteSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
             'DBED8CDE-435D-7865-76FE-149AA54AC7F7',],
            'type': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteSyncRules', body)

    def testListSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'group_uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listSyncRules', body)

    def testListSyncRulesStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [ 'bb879aCB-6FD5-DCD1-d8E6-593A31EB9cEC', '38bcE2De-A5D8-3FD9-fc3A-5e238CF772b3',],
        }
        syncRules = SyncRules(a)
        r = syncRules.listSyncRulesStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listSyncRulesStatus', body)

    def testDescribeSyncRulesMrtg(self):
        a = Auth(username, pwd)
        body = {
            'set_time': 1,
            'type': '',
            'interval': '时间间隔',
            'set_time_init': '',
            'rule_uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesMrtg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesMrtg', body)

    def testDescribeSyncRulesIncreDdl(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': 'f706174B-6B1f-8b06-9AA9-9ee53797EFbF',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRulesIncreDdl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRulesIncreDdl', body)

    def testDescribeSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'd4CAc4AD-6bb1-1dF4-Dd2D-339eD7DaCbfd',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSyncRules', body)

    def testListObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjCmp', body)

    def testCreateObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'obj_cmp_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cal_table_recoders': 1,
            'cmp_type': 'user',
            'rule_uuid': '751A03F5-C97D-645B-82B2-316A5D198528',
            'db_user_map': {'src_user':'dst_user'},
            'policies': '',
            'policy_type': 'periodic',
            'one_time': '2019-05-27 16:07:08',
            'repair': 1,
        }
        syncRules = SyncRules(a)
        r = syncRules.createObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createObjCmp', body)

    def testDeleteObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [ '11111111-1111-1111-1111-111111111111',],
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteObjCmp', body)

    def testDescribeObjCmp(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.describeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeObjCmp', body)

    def testListObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'f961C905-FECF-cC2d-aCc8-C8f0F7933ddD',
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjCmpResultTimeList', body)

    def testDescribeObjCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'CdDAb3C3-cB8F-1dDe-6DcD-9BC94DbaFA25',
            'start_time': '',
            'limit': 1,
            'offset': '',
            'search_value': '',
            'BackLackOnly': 0,
        }
        syncRules = SyncRules(a)
        r = syncRules.describeObjCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeObjCmpResult', body)

    def testDescribeObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '17DAb2db-DD91-b86a-BE24-BA55A76CB6E1',
            'time_list': [],
        }
        syncRules = SyncRules(a)
        r = syncRules.describeObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeObjCmpResultTimeList', body)

    def testListObjCmpCmpInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_value': '',
            'usr': 'I2',
            'filed': '',
            'uuid': '',
            'start_time': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjCmpCmpInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjCmpCmpInfo', body)

    def testListObjCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjCmpStatus', body)

    def testCreateObjFix(self):
        a = Auth(username, pwd)
        body = {
            'obj_fix_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'rule_uuid': '751A03F5-C97D-645B-82B2-316A5D198528',
            'obj_map': [
                {'type': 'owner.name'},],
        }
        syncRules = SyncRules(a)
        r = syncRules.createObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createObjFix', body)

    def testDescribeObjFix(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '3Fb371dE-5cd9-ce5B-301D-BaDBAe3d7A2c',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeObjFix', body)

    def testDeleteObjFix(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '82aECEBF-f5e0-8Fd7-c4e6-3cC414CC55AB',
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteObjFix', body)

    def testListObjFix(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjFix', body)

    def testDescribeObjFixResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'b16D2e6B-9FEE-D78D-347B-4F060fcDEA1c',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeObjFixResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeObjFixResult', body)

    def testListObjFixStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        syncRules = SyncRules(a)
        r = syncRules.listObjFixStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listObjFixStatus', body)

    def testCreateTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_name': 'ctt->ctt',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cmp_type': 'user,table,db',
            'db_user_map': '{"CTT":"CTT"}',
            'filter_table': '[用户.表名]',
            'db_tb_map': '表映射',
            'dump_thd': 1,
            'rule_uuid': 'b395B32C-a84f-fF58-C952-F8f7dE82CdC2',
            'polices': '"0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
             'hh.ww',],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'repair': 0,
            'fix_related': 0,
        }
        syncRules = SyncRules(a)
        r = syncRules.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createTbCmp', body)

    def testDescribeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'ccdBbf97-7E4e-2D84-49Dc-A99d4DFC6f03',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeTbCmp', body)

    def testDeleteTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'fF16A5Df-022E-DfD2-96C1-88158ADbFbDB',
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteTbCmp', body)

    def testListTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listTbCmp', body)

    def testListTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'b64eCfbf-B67A-5F1D-DbFD-782fDAC7c6ad',
        }
        syncRules = SyncRules(a)
        r = syncRules.listTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listTbCmpStatus', body)

    def testListTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listTbCmpResultTimeList', body)

    def testDescribeTbCmpResuluTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': 'EBEbD8DF-Cb66-e28F-bAfC-05D21B9Dc95C',
            'uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeTbCmpResuluTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeTbCmpResuluTimeList', body)

    def testDescribeTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '30591d54-ec6c-1EA3-037d-E60DDfBd388D',
            'start_time': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeTbCmpResult', body)

    def testDescribeTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'f0Cb2a29-c07c-0C53-0e19-Bdfc7E9df16b',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeTbCmpErrorMsg', body)

    def testDescribeTbCmpCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeTbCmpCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeTbCmpCmpResult', body)

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'b2FEFeBD-8Ee3-1e26-eF7e-8D16EcaB5b1d',
            'start_val': 1000,
            'scan_ip': [
            'c01D7F86-A631-b79f-E2AA-7ccb7f2bE851',
            'c01D7F86-A631-b79f-E2AA-7ccb7f2bE851',
             'c01D7F86-A631-b79f-E2AA-7ccb7f2bE851',],
            'hosts': [
                {
            'ip': '192.168.12.200',
            'password': ''
                },],
            'use_ip_sw': 1,
        }
        syncRules = SyncRules(a)
        r = syncRules.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createBkTakeover', body)

    def testDescribeBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.describeBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeBkTakeover', body)

    def testDeleteBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'eF5De34D-9Fc0-f26F-Db4F-31FbeBAAEEeA',
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': 'fC304CF1-c7Ac-C28C-9b73-7F15bd59aCE7',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeBkTakeoverResult', body)

    def testListBkTakeoverStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        syncRules = SyncRules(a)
        r = syncRules.listBkTakeoverStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listBkTakeoverStatus', body)

    def testListBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.listBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listBkTakeover', body)

    def testCreateReverse(self):
        a = Auth(username, pwd)
        body = {
            'reverse_name': '',
            'rule_uuid': '94ADbD94-A8bA-2E9B-dF2b-490546F247dd',
            'node_uuid': '57dA0abC-7ed6-ecDF-346F-eab1D812A9FD',
            'start_scn': 1,
        }
        syncRules = SyncRules(a)
        r = syncRules.createReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'createReverse', body)

    def testDeleteReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        syncRules = SyncRules(a)
        r = syncRules.deleteReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'deleteReverse', body)

    def testDescribeReverse(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '8E5771C8-7C17-e7C3-EC3e-AdDc46e641b9',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeReverse', body)

    def testListReverse(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listReverse', body)

    def testListReverseStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '416Bd2d7-9eEc-f9D2-D6fB-B95d028E0b07',
        }
        syncRules = SyncRules(a)
        r = syncRules.listReverseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listReverseStatus', body)

    def testStopReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '16c27383-98Fd-2fAe-7C4c-8cD1c4d2eA22',
        }
        syncRules = SyncRules(a)
        r = syncRules.stopReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'stopReverse', body)

    def testRestartReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '6BbFE709-B6C5-707b-d118-67c1D8C311d2',
        }
        syncRules = SyncRules(a)
        r = syncRules.restartReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'restartReverse', body)

    def testDescribeSingleReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '22Dd7D6c-2d3B-4Ddf-b271-5C6E23C08cd4',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeSingleReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeSingleReverse', body)

    def testDescribeRuleSelectUser(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '17D1c8CA-4E86-BBF6-7e59-F2FaC9e3d63C',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleSelectUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleSelectUser', body)

    def testDescribeRuleZStructure(self):
        a = Auth(username, pwd)
        body = {
            'tab': 'e90Ed812-4223-8bfD-0694-d055BEb463ef',
            'user': '',
            'db_uuid': '5c8A8D9F-cdE8-45dd-6BEb-12B793eAeC9b',
            'lv': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleZStructure(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleZStructure', body)

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '',
            'date_end': '',
            'type': 1,
            'module_type': 1,
            'query_type': 1,
            'rule_uuid': 'f3b7E814-d57F-E564-31Ff-Ac0BF5f8DfEb',
        }
        syncRules = SyncRules(a)
        r = syncRules.listRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listRuleLog', body)

    def testDescribeRuleTableFix(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'a04CCBeC-b3DF-7b97-8fAd-AdD461B9D74d',
            'tab': [],
            'fix_relation': 0,
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleTableFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleTableFix', body)

    def testListRuleSyncTable(self):
        a = Auth(username, pwd)
        body = {
            'row_uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.listRuleSyncTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listRuleSyncTable', body)

    def testListRuleIncreDml(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': 'EeECDC74-35f4-fEAF-c9F9-11c56e5A4CF4',
        }
        syncRules = SyncRules(a)
        r = syncRules.listRuleIncreDml(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listRuleIncreDml', body)

    def testDescribeRuleGetFalseRule(self):
        a = Auth(username, pwd)
        body = {
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleGetFalseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleGetFalseRule', body)

    def testDescribeRuleGetScn(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '8CD61f28-F06F-7bFf-697C-26fA70f045Bd',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleGetScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleGetScn', body)

    def testListRuleLoadReport(self):
        a = Auth(username, pwd)
        body = {
            'type': 'sec',
            'start_time': '',
            'end_time': '',
            'limit': 10,
            'offset': 0,
            'uuid': '1d2F6Fed-DAC6-FE94-A6cB-5Ab55415E9fd',
        }
        syncRules = SyncRules(a)
        r = syncRules.listRuleLoadReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listRuleLoadReport', body)

    def testListRuleLoadDelayReport(self):
        a = Auth(username, pwd)
        body = {
            'type': 'sec',
            'start_time': '',
            'end_time': '',
            'limit': 10,
            'offset': 0,
            'uuid': '1d2F6Fed-DAC6-FE94-A6cB-5Ab55415E9fd',
        }
        syncRules = SyncRules(a)
        r = syncRules.listRuleLoadDelayReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'listRuleLoadDelayReport', body)

    def testDescribeRuleDbCheck(self):
        a = Auth(username, pwd)
        body = {
            'src_db_uuid': '',
            'dst_db_uuid': '',
        }
        syncRules = SyncRules(a)
        r = syncRules.describeRuleDbCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRules', 'describeRuleDbCheck', body)


if __name__ == '__main__':
    unittest.main()  
