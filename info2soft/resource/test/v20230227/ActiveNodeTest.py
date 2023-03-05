
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.resource.v20230227.ActiveNode import ActiveNode
# from info2soft.resource.v20200722.ActiveNode import ActiveNode
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


class ActiveNodeTestCase(unittest.TestCase):

    def testListInactiveNodes(self):
        a = Auth(username, pwd)
        body = {
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.listInactiveNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listInactiveNodes', body)

    def testActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': 'Jason Rodriguez',
            'address': '163.198.38.25',
            'data_port': '26804',
            'cache_dir': '/var/i2data/cache/',
            'ipctoken': 'ba8C2C5c-d623-fFEF-13d6-Bf3759EAEb1C',
            'log_dir': '/var/i2data/log/',
            'registered': 0,
            'comment': 'string',
            'web_uuid': '912396eB-A20f-f26e-88c4-9fCF851f573f',
            'port': {
            'iarelay': '',
            'iamsk': '',
            'iasync': '',},
            'maintenance': 0,
            'node_type': '',
            'phy_type': '',
            'biz_grp_list': [],
            'cluster_switch': 1,
            'node_uuids': '',
            'node_cluster_type': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.activeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'activeNode', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '73d4f3Ca-F6F1-aEd7-cd78-d2A3AacED8Da',
            'f5ACde9F-171F-E1e4-cD6d-fDB9FC1588F4',],
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listNodeStatus', body)

    def testListNodes(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'nodetype': 'name',
            'search_field': '',
            'order_by': '',
            'sort': 'name',
            'search_value': '',
            'where_args': '["node_cluster_type"=1]',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.listNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listNodes', body)

    def testDescriptNode(self):
        a = Auth(username, pwd)
        body = {
            'registered': 1,
            'uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        activeNode = ActiveNode(a)
        r = activeNode.descriptNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'descriptNode', body)

    def testDescriptNodeDebugInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '41D1C1E8-60AE-4853-9694-5599560EEB0F',
            'last_time': 1,
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.descriptNodeDebugInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'descriptNodeDebugInfo', body)

    def testModifyNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': 'Kenneth Wilson',
            'address': '192.168.12.199',
            'data_port': '26804',
            'cache_dir': '/var/i2data/cache/',
            'iptoken': '780B4F1B-6FB9-46C4-98AC-02A8DF4A1C76',
            'log_dir': '/var/i2data/log/',
            'node_uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
            'registered': 1,
            'comment': 'string',
            'web_uuid': 'edE462DA-bbCC-68d3-4B3d-264abF03EcB7',
            'port': {
            'iarelay': '26806',
            'iamask': '26808',
            'iasync': '26803',},
            'maintenance': 0,
            'node_type': '1111010000',
            'phy_type': '2',
            'os_type': '0',
            'biz_grp_list': [],
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.modifyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'modifyNode', body)

    def testDeleteNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '1E5a57F3-1a6e-DfeE-5fB2-FddF7E1d1Ceb',
            '5d8BDEAC-8eBc-7eF5-FA7F-6cE47C77EdBE',],
            'force': 0,
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.deleteNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'deleteNode', body)

    def testUpgradeNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'fcD5B349-e2DE-1faB-3B7D-d9E621C1C215',],
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'upgradeNode', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'switchMaintenance', body)

    def testGetCharset(self):
        a = Auth(username, pwd)
        body = {
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.getCharset(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'getCharset', body)

    def testSwitchDbMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.switchDbMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'switchDbMaintenance', body)

    def testDescribeDbHealthInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'bfe3379E-9e6c-513e-6eFf-8F3FAD9cCbdA',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.describeDbHealthInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'describeDbHealthInfo', body)

    def testListDbs(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'db_name',
            'search_value': '',
            'role': '',
            'direction': '',
            'db_type': '',
            'ip': '',
            'port': '',
            'service_name': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.listDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listDbs', body)

    # def testCheckDbLink(self):
    #     a = Auth(username, pwd)
    #     body = {
    #         'db_name': 'Laura Lopez',
    #         'node_uuid': '778553A7-9A06-4F05-AB40-8BD59F353D62',
    #         'db_type': 'oracle',
    #         'file_open_type': 'DIRECT',
    #         'deploy_mode': 'single',
    #         'log_read_type': 'file',
    #         'config': {
    #         'username': 'Lisa Hernandez',
    #         'password': 'i2',
    #         'server_name': 'orcl',
    #         'port': 1521,
    #         'log_read': {
    #         'os_auth': 1,
    #         'asm_instance': '',
    #         'asm_username': '',
    #         'asm_port': 1521,
    #         'asm_password': '12323131',},
    #         'filter_session': 1,
    #         'relay': {
    #         'enable': 1,
    #         'relay_node_uuid': '',},
    #         'remote_file_agent': {
    #         'enable': 1,
    #         'port': 1,
    #         'compress': 'none',},
    #         'db_list': [{
    #         'ip': '44.223.79.91',
    #         'thread': '1',
    #         'disable': '1',},],
    #         'broker_server': [{
    #         'ip': '229.14.214.160',
    #         'port': 8080,},],
    #         'charset': '',
    #         'kafka_auth_type': 'none',
    #         'kerberos_keytab_path': '',
    #         'kerberos_principal': '',
    #         'kerberos_service_name': '',
    #         'kudu_impala': {
    #         'impala_server_ip': '158.12.5.46',
    #         'impala_server_port': '21050',
    #         'impala_auth_type': '',
    #         'default_database': '',
    #         'impala_client_keytab_path': '',
    #         'impala_client_krb_principal': '',
    #         'impala_server_krbhost_fqdn': '',
    #         'impala_server_krbrealm': '',
    #         'impala_server_krbservice_name': '',},
    #         'db_schema': 'oracle',},
    #         'db_uuid': '6C4AEF37-6496-6DCD-E085-DD640001E4EC',
    #         'node_type': '1110001000',
    #         'db_mode': 'normal',
    #     }
    #
    #     activeNode = ActiveNode(a)
    #     r = activeNode.checkDbLink(body)
    #     print(r[0])
    #     assert r[0]['ret'] == 200
    #     write(r[0], 'ActiveNode', 'checkDbLink', body)

    def testCheckDbLink(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'type': 'oracle',
            'conf': [{
            'id': 1,
            'name': 'kfk',
            'ip': '172.20.5.116',
            'port': '1521',
            'auth': 'none',
            'pass': {
            'user': 'i2',
            'pass': 'i2',},
            'kerberos': {
            'principal': '',
            'keytab': '',},
            'impala': {
            'ip': '',
            'port': '',
            'name': '',
            'auth': 'kerberos',
            'kerberos': {
            'realm': '',
            'name': '',
            'host': '',
            'principal': '',
            'keytab': '',},},
            'model': '0',
            'sniff': '0',},{
            'id': 2,
            'name': 'oracle',
            'ip': '172.20.5.116',
            'port': '1521',
            'auth': 'pass',
            'pass': {
            'user': 'i2',
            'pass': 'i2',},
            'kerberos': {
            'principal': '',
            'keytab': '',},
            'impala': {
            'ip': '',
            'port': '',
            'name': '',
            'auth': '',
            'kerberos': {
            'realm': '',
            'name': '',
            'host': '',
            'principal': '',
            'keytab': '',},},
            'model': '1',
            'sniff': '1',},{
            'id': 3,
            'name': 'kfk',
            'ip': '172.20.5.116',
            'port': '1521',
            'auth': 'kerberos',
            'pass': {
            'user': '',
            'pass': '',},
            'kerberos': {
            'principal': '',
            'keytab': '',},
            'impala': {
            'ip': '',
            'port': '',
            'name': '',
            'auth': '',
            'kerberos': {
            'realm': '',
            'name': '',
            'host': '',
            'principal': '',
            'keytab': '',},},
            'model': '0',
            'sniff': '0',},{
            'id': 4,
            'name': 'kudu',
            'ip': '172.20.5.116',
            'port': '1521',
            'auth': 'none',
            'pass': {
            'user': '',
            'pass': '',},
            'kerberos': {
            'principal': '',
            'keytab': '',},
            'impala': {
            'ip': '',
            'port': '',
            'name': '',
            'auth': 'kerberos',
            'kerberos': {
            'realm': '',
            'name': '',
            'host': '',
            'principal': '',
            'keytab': '',},},
            'model': '1',
            'sniff': '1',},],
            'jsonver': {},
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.checkDbLink(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'checkDbLink', body)

    def testListDbStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'd6dDB478-0dBc-2747-6b13-bfcf3f6569Eb',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.listDbStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listDbStatus', body)

    def testCreateDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Ronald Wilson',
            'node_uuid': '5BF86fdF-9F3d-69CE-55bD-5ffF1Cbe1bdB',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Edward Brown',
            'password': '',
            'server_name': '',
            'port': 1,
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'no',},
            'db_list': [{
            'ip': '',
            'thread': '',
            'disable': 1,},],
            'producer_host': '25.254.57.56',
            'producer_port': 1,
            'broker_server': [{
            'ip': '7.99.161.172',
            'port': 1,},],
            'authentication': 'none',
            'principal': '',
            'keytabfile': '',
            'kafka_auth_type': '',
            'kerberos_keytab_path': '',
            'kerberos_principal': '',
            'kerberos_service_name': '',
            'sasl_plain_user': '',
            'sasl_plain_pass': '',
            'sqlserver': {
            'ip': '',
            'port': 1,
            'usr': '',
            'pwd': '',
            'db': '',
            'dacport': '',},
            'user_management': [{
            'user': '',
            'passwd': '',
            'default_db': '',
            'cred_uuid': '',
            'cred_login': 1,
            'certificate': '',},],
            'db_ip': '',
            'model': 1,
            'sniff': '',
            'role': [{
            'source': 0,
            'target': 1,},],
            'login_url': '',
            'conn_pool_max': 1,
            'instance_name': '',
            'database_name': '',
            'jks': '',
            'kerberos_keytab_auth': '',
            'user_oceanbase': '',
            'db2_run_system': '',
            'ssl_switch': 0,},
            'db_uuid': 'FaA7e66B-6FAB-C3F7-5A5C-beDDA3E92729',
            'db_mode': '',
            'cdb': 'E37cbCeF-Fc61-f95E-DaaE-1797BA6ade29',
            'biz_grp_list': [],
            'maintenance': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.createDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'createDb', body)

    def testCreateDbUnified(self):
        a = Auth(username, pwd)
        body = {
            'biz_grp_list': [],
            'db_name': 'Paul Wilson',
            'node_uuid': 'F5F4D75D-a0de-bf54-93Ab-6efBcE19b936',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'model': 1,
            'sniff': '',
            'user_management': [{
            'user': '',
            'passwd': '',
            'default_db': '',
            'cred_uuid': '',
            'cred_login': 1,
            'url': '',
            'auth_uuid': '',},],
            'role': [{
            'source': 0,
            'target': 1,},],
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'no',},
            'db_list': [{
            'disable': 0,
            'ip': '',
            'thread': '',
            'port': '',
            'http_port': '',},],
            'transport': {
            'auth': '',
            'ssl_mode': '',
            'certificate': '',},
            'auth': '',
            'replication_num': '',},
            'db_uuid': '3BEaa2CC-E39D-3B64-30a2-F61c493FfEf1',
            'db_mode': '',
            'cdb': 'BB7fC7CD-563F-F24b-Fc12-00cD6101bE2b',
            'maintenance': '',
            'password': '',
            'comment': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.createDbUnified(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'createDbUnified', body)

    def testModifyDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Kevin Moore',
            'db_uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
            'node_uuid': '0596a77C-64Fd-cAf2-DB9c-cAaeBD56eD88',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'George White',
            'password': '',
            'server_name': '',
            'port': 1,
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'no',},
            'db_list': [{
            'ip': '',
            'thread': '',},],
            'broker_server': ' ',
            'conn_pool_max': 1,
            'instance_name': '',
            'database_name': '',},
            'random_str': '',
            'cdb': '41e7BE6e-CF65-5b58-c251-91c84222efda',
            'maintenance': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        activeNode = ActiveNode(a)
        r = activeNode.modifyDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'modifyDb', body)

    def testDescribeDbSpace(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.describeDbSpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'describeDbSpace', body)

    def testDeleteDb(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'A0A0526D-6503-5C2A-E3D8-7D85813967F1',],
            'force': 0,
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.deleteDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'deleteDb', body)

    def testBatchCreateDbs(self):
        a = Auth(username, pwd)
        body = {
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.batchCreateDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'batchCreateDbs', body)

    def testDescribeDb(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        activeNode = ActiveNode(a)
        r = activeNode.describeDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'describeDb', body)

    def testRebuildActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.rebuildActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'rebuildActiveNode', body)

    def testRefresgActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'xxxxxxxxx',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.refresgActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'refresgActiveNode', body)

    def testRestartAllProcess(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        activeNode = ActiveNode(a)
        r = activeNode.restartAllProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'restartAllProcess', body)


if __name__ == '__main__':
    unittest.main()
