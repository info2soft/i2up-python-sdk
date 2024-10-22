
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Rabbitmq
from info2soft.active.v20240819.Rabbitmq import Rabbitmq
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


class RabbitmqTestCase(unittest.TestCase):

    def testListRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.listRabbitmqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'listRabbitmqRule', body)

    def testCreateRabbitMqRule(self):
        a = Auth(username, pwd)
        body = {
            'start_rule_now': 1,
            'rule_name': '12321',
            'src_db_uuid': '2C4C2E77-774D-C604-9A32-5038D8E590C4',
            'tgt_type': 'db2',
            'tgt_db_uuid': '953C47CB-3F6C-E72F-DF1C-31522468A566',
            'map_type': 'db',
            'db_user_map': '',
            'table_map': '',
            'dbmap_topic': '',
            'row_map_mode': 'rowid',
            'sync_mode': 1,
            'start_scn': '',
            'kafka_time_out': '120000',
            'part_load_balance': 'by_table',
            'kafka_message_encoding': 'UTF-8',
            'kafka': {
            'binary_code': 'hex',},
            'dml_track': {
            'enable': 0,
            'urp': 0,
            'drp': 0,
            'tmcol': '',
            'delcol': '',},
            'storage_settings': {
            'src_max_mem': '512',
            'src_max_disk': '5000',
            'txn_max_mem': '10000',
            'tf_max_size': '100',
            'max_ld_mem': '512',
            'tgt_extern_table': '',},
            'other_settings': {
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'fill_lob_column': 0,
            'keep_seq_sync': 0,
            'keep_usr_pwd': 0,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'gen_txn': 0,},
            'error_handling': {
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'drp': 'ignore',
            'load_err_set': 'continue',
            'report_failed_dml': 0,},
            'bw_settings': {
            'bw_limit': '',},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': [],
            'table_space_name': [],},
            'full_sync_settings': {
            'load_mode': 'direct',
            'ld_dir_opt': 0,
            'dump_thd': 1,
            'load_thd': 1,
            'try_split_part_table': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'concurrent_table': '[]',},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [],},
            'filter_table_settings': {
            'exclude_table': '[]',},
            'etl_settings': {
            'etl_table': [],},
            '_': '489d781db90cb',
            'encrypt': '',
            'encrypt_switch': 1,
            'compress': 1,
            'compress_switch': 1,
            'compress_algo': '',
            'compress_level': '',
            'secret_key': '',
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.createRabbitMqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'createRabbitMqRule', body)

    def testModifyRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.modifyRabbitmqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'modifyRabbitmqRule', body)

    def testDescribeRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.describeRabbitmqRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'describeRabbitmqRule', body)

    def testDeleteRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'type': '',
            'force': 0,
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.deleteRabbitmqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'deleteRabbitmqRule', body)

    def testResumeRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'scn': '',
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.resumeRabbitmqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'resumeRabbitmqRule', body)

    def testStopRabbitmqRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
            'scn': '',
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.stopRabbitmqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'stopRabbitmqRule', body)

    def testListSyncRulesStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        rabbitmq = Rabbitmq(a)
        r = rabbitmq.listSyncRulesStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Rabbitmq', 'listSyncRulesStatus', body)


if __name__ == '__main__':
    unittest.main()
