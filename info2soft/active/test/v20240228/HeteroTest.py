# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20240228.Hetero import Hetero
# from info2soft.active.v20200722.Hetero import Hetero
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


class HeteroTestCase(unittest.TestCase):

    def testCreateConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'name': 'Joseph Brown',
            'src_db_uuid': 'B5CED857-275C-77C4-0561-887F7C890FF2',
            'tgt_type': 'oracle',
            'topic': 'test1',
            'dst_topic': 'topic1',
            'tgt_db_uuid': '1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'init_offset_type': 'earlist',
            'consumer_thread_num': 2,
            'actload_thread_num': 4,
            'kudu_partition_config': [],
            'impala_connected': '',
        }

        hetero = Hetero(a)
        r = hetero.createConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'createConsumerRule', body)

    def testModifyConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'init_offset_type': 'seek',
            'modify': 1,
            'start_rule_now': 1,
            'topic': 'test4',
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
        }

        hetero = Hetero(a)
        r = hetero.modifyConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'modifyConsumerRule', body)

    def testDeleteConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
                '5b4D9EAc-97Ca-3c3b-Cef6-4f28eA9dC271',
                '553f3Ca3-b1AA-3D2e-3dfE-bcEBAcF3f548', ],
            'force': 1,
        }

        hetero = Hetero(a)
        r = hetero.deleteConsumerRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'deleteConsumerRules', body)

    def testListConsumerStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }

        hetero = Hetero(a)
        r = hetero.listConsumerStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listConsumerStatus', body)

    def testStopConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'C63cd277-70bB-5769-9AEe-2416b7BD2454',
            'operate': 'resume',
        }

        hetero = Hetero(a)
        r = hetero.stopConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'stopConsumerRule', body)

    def testListConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'search_field': 'tgt_type',
            'limit': 1,
            'page': 1,
            'search_value': ''
        }

        hetero = Hetero(a)
        r = hetero.listConsumerRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listConsumerRules', body)

    def testDescribeConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '75DF8EA3-6480-4137-451B-731F04F368AF',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hetero = Hetero(a)
        r = hetero.describeConsumerRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'describeConsumerRules', body)

    def testCreateHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'graph_name': '',
            'is_parent': '',
            'is_rule': '',
            'consume_rule': [{
                'id': '',
                'rule_number': 1,
                'rule_name': '',
                'src_type': '',
                'src_uuid': '',
                'dst_type': '',
                'dst_uuid': '',
                'rule_status': '',
                'is_parent': '',
                'is_rule': '',
                'src_name': '',
                'dst_name': '',
                'rule_traffic': '', }, ],
        }

        hetero = Hetero(a)
        r = hetero.createHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'createHeteroGraph', body)

    def testAddHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'graph_uuid': '',
            'rule_number': '',
            'src_type': '',
            'rule_uuid': '',
        }

        hetero = Hetero(a)
        r = hetero.addHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'addHeteroGraph', body)

    def testListHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }

        hetero = Hetero(a)
        r = hetero.listHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listHeteroGraph', body)

    def testRunHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'graphs': [],
            'graph_uuid': '',
            'rule_uuids': [{
                'uuid': '',
                'src_type': '', }, ],
        }

        hetero = Hetero(a)
        r = hetero.runHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'runHeteroGraph', body)

    def testStopHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'graphs': [{
                'graph_uuid': '',
                'rule_uuids': [{
                    'uuid': '',
                    'src_type': '', }, ], }, ],
        }

        hetero = Hetero(a)
        r = hetero.stopHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'stopHeteroGraph', body)

    def testListGraphStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }

        hetero = Hetero(a)
        r = hetero.listGraphStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listGraphStatus', body)

    def testDeleteHeteroGraph(self):
        a = Auth(username, pwd)
        body = {
            'graph_uuids': [{
                'graph_uuid': 'e0C7c7C8-5365-356B-b35e-2a69ADe91e6d',
                'rule_uuids': [{
                    'uuid': 'e5CBcEd6-f93c-5Ab3-76C2-e3b1FEF3AD58',
                    'is_rule': '1',
                    'rule_number': '4',
                    'src_type': 'oracle', }, ], }, ],
            'is_whole': '1',
        }

        hetero = Hetero(a)
        r = hetero.deleteHeteroGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'deleteHeteroGraph', body)

    def testDescriptGraphDetail(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'start_time': '',
            'end_time': '',
            'graph_uuid': '',
        }

        hetero = Hetero(a)
        r = hetero.descriptGraphDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'descriptGraphDetail', body)

    def testListGraph(self):
        a = Auth(username, pwd)
        body = {
            'graph_uuid': '',
        }

        hetero = Hetero(a)
        r = hetero.listGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listGraph', body)

    def testCreateHeteroRule(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'kfk_ver': '',
            'dst_node': '',
            'conn_type': '',
            'host': '',
            'port': '',
            'broker': '',
            'tabmap': {},
            'consumer_thread_num': 2,
            'actload_thread_num': 4,
        }

        hetero = Hetero(a)
        r = hetero.createHeteroRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'createHeteroRule', body)

    def testConsumer(self):
        a = Auth(username, pwd)
        body = {
            'topic': '',
            'offset': '',
            'lines': '',
            'show_foward': 1,
        }

        hetero = Hetero(a)
        r = hetero.consumer(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'consumer', body)

    def testDeleteHeteroRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }

        hetero = Hetero(a)
        r = hetero.deleteHeteroRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'deleteHeteroRule', body)

    def testCreateConsumer(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        hetero = Hetero(a)
        r = hetero.createConsumer(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'createConsumer', body)

    def testCreateHeteroTopic(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        hetero = Hetero(a)
        r = hetero.createHeteroTopic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'createHeteroTopic', body)

    def testListHeteroRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'kafka_name',
            'search_value': '',
        }

        hetero = Hetero(a)
        r = hetero.listHeteroRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Hetero', 'listHeteroRule', body)


if __name__ == '__main__':
    unittest.main()
