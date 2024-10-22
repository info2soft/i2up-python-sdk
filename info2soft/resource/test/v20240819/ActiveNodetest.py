
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ActiveNode
from info2soft.resource.v20240819.ActiveNode import ActiveNode
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
            'node_name': 'Donald Williams',
            'address': '55.18.241.141',
            'data_port': 26804,
            'cache_dir': '/var/i2data/cache/',
            'password': 'A34fcB6E-d44b-63dE-9A3E-31EEAd41cefd',
            'log_dir': '/var/i2data/log/',
            'registered': 1,
            'comment': 'string',
            'web_uuid': 'C82Aed4a-d95C-C1Fc-fcdB-73615fBED36F',
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
            '64e8Bd28-5fa3-4BCD-55bB-FB9bFf4Fca3f',
            '2fD3Acff-67F7-fE9E-b5E8-7edAdC0Ca1af',],
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
            'sort': '@pick{"name", "address"}',
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
            'node_name': 'Ronald Hall',
            'address': '192.168.12.199',
            'data_port': 26804,
            'cache_dir': '/var/i2data/cache/',
            'iptoken': '780B4F1B-6FB9-46C4-98AC-02A8DF4A1C76',
            'log_dir': '/var/i2data/log/',
            'node_uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
            'registered': 1,
            'comment': 'string',
            'web_uuid': '0B81b82c-C67b-4F6A-A096-2343DC52543b',
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
            '8A46c1F5-ABDc-85D7-26ce-1C1bC1fe7eB8',
            '3efEF0F3-BA97-67b3-Ed48-46db4Be872Ec',],
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
            '86e756c5-A9aA-dFda-72Ad-D23FE9D78Baa',],
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
            '556F698D-ecd7-26bC-e40B-d4e39b1934E3',],
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
            'uuids': '0AAff5db-F2fD-939c-ed24-7EEcd412C2De',
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
            'db_name': 'Melissa Lewis',
            'node_uuid': 'db7FA79e-fCA9-92af-fe82-9EfC986EE612',
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
            'db_uuid': 'Eed9dD81-9dA2-8EEe-df1b-9f59Fbc5C4c6',
            'db_mode': '',
            'cdb': '8C3c7da6-2714-AbFB-2FBE-08b68A1f3292',
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
            'db_name': 'Brian Young',
            'db_uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
            'node_uuid': '0596a77C-64Fd-cAf2-DB9c-cAaeBD56eD88',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Ruth Garcia',
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
            'cdb': '7C86fcE5-47BF-3DDC-AdeC-7A09B91F3cBe',
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
