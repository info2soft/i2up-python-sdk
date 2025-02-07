
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ActiveNode
from info2soft.resource.v20250123.ActiveNode import ActiveNode
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
            'node_name': 'David Smith',
            'address': '168.85.226.75',
            'data_port': 26804,
            'cache_dir': '/var/i2data/cache/',
            'password': '6b7DbfBF-5Cdd-Cebe-Ed2b-6D8093C12018',
            'log_dir': '/var/i2data/log/',
            'registered': 0,
            'comment': 'string',
            'web_uuid': 'AE38433B-c6D7-AdC5-754e-69FdFfB7A6DD',
            'port': {
            'iarelay': '',
            'iamsk': '',
            'iasync': '',},
            'maintenance': 0,
            'node_type': '',
            'phy_type': 1,
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
            'eD4fbFCF-7fC3-Cc85-1bC5-3feD6485BcBa',
            'e551dede-FD0b-2AfC-CdeF-9eB2B31ddACB',],
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
            'nodetype': '@pick{"name","source","backup"]}',
            'search_field': '',
            'order_by': '',
            'sort': "@pick{'name',address}",
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
            'node_name': 'Frank Smith',
            'address': '192.168.12.199',
            'data_port': 26804,
            'cache_dir': '/var/i2data/cache/',
            'iptoken': '780B4F1B-6FB9-46C4-98AC-02A8DF4A1C76',
            'log_dir': '/var/i2data/log/',
            'node_uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
            'registered': 1,
            'comment': 'string',
            'web_uuid': '97C2b374-6fDD-6c76-8613-C4c69fe51F08',
            'port': {
            'iarelay': '26806',
            'iamask': '26808',
            'iasync': '26803',},
            'maintenance': 0,
            'node_type': '1111010000',
            'phy_type': 2,
            'os_type': 0,
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
            'BfcC87c2-DD8C-fC62-2A23-Dfe7cfE45F85',
            'A5C7fCBD-91e8-3EcC-BFBA-B2f367eC93ab',],
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
            '13baFA7b-c3bf-Fefe-ef05-996778eFdF4B',],
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'upgradeNode', body)

    def testRenewActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'Fe5c9B7E-21B1-Dd6E-4a3c-BDa5D7f2ee3c',],
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.renewActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'renewActiveNode', body)

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
            'uuids': '185BcB88-1e8e-F6F1-5c86-932F9B4e04FA',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.listDbStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'listDbStatus', body)

    def testCreateDbUnified(self):
        a = Auth(username, pwd)
        body = {
            'biz_grp_list': [],
            'db_name': 'Daniel Hernandez',
            'node_uuid': '2A81B0D4-9307-dc3e-5982-3Dc1dFDadfFA',
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
            'replication_num': '',
            'zookeeper': {
            'set': [{
            'ip': '',
            'port': '',
            'zk_node': '',},],},
            'pdserver': [{
            'ip': '',
            'port': '',},],
            'ocp_server': [{
            'ip': '',
            'rpcport': '',
            'sqlport': '',},],
            'manual_ocp_conf': 1,
            'ob_sharding_nodes': [{
            'cluster_name': '',
            'tenant_name': '',
            'ip': '',
            'port': '',
            'tenant_user': '',
            'tenant_pass': '',
            'tenant_cred_switch': '',
            'tenant_cred_uuid': '',
            'manage_user': '',
            'manage_pass': '',
            'manage_cred_switch': '',
            'manage_cred_uuid': '',},],
            'manage_port': '',
            'ob_sharding_inst': [],
            'table_type': '',},
            'db_uuid': '0ad26bc9-9ba1-F2cD-Fbb5-bc2542ecFAb3',
            'db_mode': '',
            'cdb': 'fd9e45Bd-D60b-2f0E-4ce2-CDCfd996B228',
            'maintenance': '',
            'password': '',
            'comment': '',
            'node_type': 1,
            'cluster_uuid': '',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.createDbUnified(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'createDbUnified', body)

    def testModifyDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Gary Garcia',
            'db_uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
            'node_uuid': '0596a77C-64Fd-cAf2-DB9c-cAaeBD56eD88',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Linda Thomas',
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
            'cdb': '9dB7676f-92E4-47bE-D5f2-4D00BE8E05b1',
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
            'csv_file': '',
            'type': '',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.batchCreateDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'batchCreateDbs', body)

    def testBatchCreateActiveNodes(self):
        a = Auth(username, pwd)
        body = {
            'csv_file': '',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.batchCreateActiveNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'batchCreateActiveNodes', body)

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
            'process': [
            'iawork',
            'iaback',],
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.restartAllProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'restartAllProcess', body)

    def testGetActiveDbAuthInfo(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.getActiveDbAuthInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'getActiveDbAuthInfo', body)

    def testBatchCreateSqlserverDbs(self):
        a = Auth(username, pwd)
        body = {
            'bind_lic_list': [],
            'db_list': '',
            'db_type': '',
            'node_uuid': '',
            'prefix': '',
            'role': '',
        }
        
        
        activeNode = ActiveNode(a)
        r = activeNode.batchCreateSqlserverDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNode', 'batchCreateSqlserverDbs', body)


if __name__ == '__main__':
    unittest.main()
