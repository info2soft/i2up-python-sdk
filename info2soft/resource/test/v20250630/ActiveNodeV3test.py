
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ActiveNodeV3
from info2soft.resource.v20250630.ActiveNodeV3 import ActiveNodeV3
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


class ActiveNodeV3TestCase(unittest.TestCase):
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

    def testListDbs(self):
        a = Auth(username, pwd)
        body = {
            'search_field': 'db_name',
            'search_value': '',
            'page': 1,
            'limit': 10,
            'direction': '',
            'db_type': '',
            'ip': '',
            'port': '',
            'service_name': '',
            'role': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.listDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'listDbs', body)

    def testCheckDbLink(self):
        a = Auth(username, pwd)
        body = {
            'jsonver': {},
            'uuid': '6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'type': 'oracle',
            'conf': [{
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
            'sniff': '0',
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
            'keytab': '',},},{
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
            'sniff': '1',
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
            'keytab': '',},},{
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
            'sniff': '0',
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
            'keytab': '',},},{
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
            'sniff': '1',
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
            'keytab': '',},},],
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.checkDbLink(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'checkDbLink', body)

    def testListDbStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '2AA1B9Ad-EFef-BE5d-e5eE-c7BAf7eDf9fD',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.listDbStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'listDbStatus', body)

    def testCreateDbUnified(self):
        a = Auth(username, pwd)
        body = {
            'biz_grp_list': [],
            'db_name': 'Deborah Jackson',
            'node_uuid': 'c27ABFC1-723d-FEE3-fe27-fB5D4A5f73a7',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'zookeeper': {
            'set': [{
            'ip': '',
            'port': '',
            'zk_node': '',},],},
            'pdserver': [{
            'ip': '',
            'port': '',},],
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
            'disable': 1,
            'ip': '',
            'thread': '',
            'port': '',
            'http_port': '',},],
            'transport': {
            'auth': '',
            'ssl_mode': '',
            'certificate': '',},
            'ocp_server': [{
            'ip': '',
            'rpcport': '',
            'sqlport': '',},],
            'manual_ocp_conf': 1,
            'auth': '',
            'replication_num': '',},
            'db_uuid': '1A373341-d3a3-57b0-1cbc-E01A9cD5cdC7',
            'db_mode': '',
            'cdb': '03546Fc6-FDEc-cCd9-1b6B-13c5196Aa28b',
            'maintenance': '',
            'password': '',
            'comment': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.createDbUnified(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'createDbUnified', body)

    def testModifyDb(self):
        a = Auth(username, pwd)
        body = {
            'random_str': '',
            'db_name': 'Steven Lopez',
            'db_uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
            'node_uuid': '0596a77C-64Fd-cAf2-DB9c-cAaeBD56eD88',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'broker_server': ' ',
            'instance_name': '',
            'database_name': '',
            'conn_pool_max': 1,
            'username': 'Jason Lee',
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
            'thread': '',},],},
            'cdb': '43dcfc43-Cc5F-bB8A-c3C4-A11b4eFECF79',
            'maintenance': '',
            'password': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.modifyDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'modifyDb', body)

    def testDescribeDbSpace(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'A0A0526D-6503-5C2A-E3D8-7D85813967F1',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.describeDbSpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'describeDbSpace', body)

    def testDeleteDb(self):
        a = Auth(username, pwd)
        body = {
            'force': 0,
            'uuids': [
            'A0A0526D-6503-5C2A-E3D8-7D85813967F1',],
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.deleteDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'deleteDb', body)

    def testBatchCreateDbs(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.batchCreateDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'batchCreateDbs', body)

    def testSwitchDbMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.switchDbMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'switchDbMaintenance', body)

    def testDescribeDb(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.describeDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'describeDb', body)

    def testGetActiveDbAuthInfo(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.getActiveDbAuthInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'getActiveDbAuthInfo', body)

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
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.batchCreateSqlserverDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'batchCreateSqlserverDbs', body)

    def testGetCharset(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.getCharset(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'getCharset', body)

    def testListInactiveNodes(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.listInactiveNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'listInactiveNodes', body)

    def testActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'address': '42.28.5.228',
            'node_cluster_type': '',
            'biz_grp_list': [],
            'data_port': 26804,
            'port': {
            'iasync': '',
            'iarelay': '',
            'iamsk': '',},
            'cache_dir': '/var/i2data/cache/',
            'cluster_switch': 1,
            'node_uuids': '',
            'password': 'C5E0dE5B-fc6A-cc9C-2A97-e1E0F9A33C2D',
            'node_type': '',
            'phy_type': 1,
            'log_dir': '/var/i2data/log/',
            'registered': 0,
            'maintenance': 0,
            'node_name': 'Steven Lee',
            'comment': 'string',
            'web_uuid': 'Cf055A55-cd3B-8A7E-623B-C62F9daF6D44',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.activeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'activeNode', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'A659D30b-4Ae2-D9eA-d025-2474EEC4A1bB',
            '6BcF04b8-422A-AcFf-cCfa-a92B5126Fb8f',],
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'listNodeStatus', body)

    def testListNodes(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'order_by': '',
            'sort': "@pick{'name',address}",
            'page': 1,
            'limit': 10,
            'search_value': '',
            'where_args': '["node_cluster_type"=1]',
            'nodetype': '@pick{"name","source","backup"]}',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.listNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'listNodes', body)

    def testDescriptNode(self):
        a = Auth(username, pwd)
        body = {
            'registered': 0,
            'uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.descriptNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'descriptNode', body)

    def testDescriptNodeDebugInfo(self):
        a = Auth(username, pwd)
        body = {
            'last_time': 1,
            'uuid': '41D1C1E8-60AE-4853-9694-5599560EEB0F',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.descriptNodeDebugInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'descriptNodeDebugInfo', body)

    def testModifyNode(self):
        a = Auth(username, pwd)
        body = {
            'address': '192.168.12.199',
            'biz_grp_list': [],
            'data_port': 26804,
            'cache_dir': '/var/i2data/cache/',
            'node_type': '1111010000',
            'phy_type': 2,
            'iptoken': '780B4F1B-6FB9-46C4-98AC-02A8DF4A1C76',
            'os_type': 0,
            'log_dir': '/var/i2data/log/',
            'node_uuid': '31424826-A97D-4085-81AE-FD64EC58B6CE1',
            'registered': 1,
            'port': {
            'iasync': '26803',
            'iarelay': '26806',
            'iamask': '26808',},
            'maintenance': 0,
            'comment': 'string',
            'web_uuid': 'A5ACDBF2-Cd80-BDCf-3def-beE8C8C0461D',
            'node_name': 'Charles Brown',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.modifyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'modifyNode', body)

    def testDeleteNode(self):
        a = Auth(username, pwd)
        body = {
            'force': 0,
            'uuids': [
            'E2D7d2F8-42CB-6B8a-63ED-ceE1B0Fe8Fd6',
            '5EE21dDD-69Fc-FB6f-4C8A-4F54fBAdd163',],
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.deleteNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'deleteNode', body)

    def testUpgradeNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '1525F053-1eFA-EFF2-780F-ABabCFD25ee3',],
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'upgradeNode', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'switchMaintenance', body)

    def testRebuildActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.rebuildActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'rebuildActiveNode', body)

    def testRefresgActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'xxxxxxxxx',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.refresgActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'refresgActiveNode', body)

    def testRestartAllProcess(self):
        a = Auth(username, pwd)
        body = {
            'process': [
            'iawork',
            'iaback',],
            'uuid': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.restartAllProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'restartAllProcess', body)

    def testDownloadFile(self):
        a = Auth(username, pwd)
        body = {
            'type': 'download',
            'file': '',
        }
        
        
        activeNodeV3 = ActiveNodeV3(a)
        r = activeNodeV3.downloadFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeV3', 'downloadFile', body)


if __name__ == '__main__':
    unittest.main()
