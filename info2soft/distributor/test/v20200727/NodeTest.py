
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import DistributorNode as Node
# from info2soft.distributor.v20200722.Node import Node
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
    
                
class NodeTestCase(unittest.TestCase):

    def testReadme(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '278D0E2C-2156-3F7F-D75F-2628E46F6B35',
            'node_name': '',
            'node_version': '4.0-19110518',
            'log_day': 10,
            'os_type': 0,
            'group_uuid': '',
            'group_name': '',
            'user_uuid': '278D0E2C-2156-3F7F-D75F-2628E46F6B35',
            'username': 'xxx',
            'system_time': 1577160228,
            'create_time': 1577160228,
            'node_type': 1,
            'node_role': 1,
            'node_addr': [{
            'ip': '172.20.2.75',
            'port': 1234,},],
            'parent_addr': [{
            'ip': '172.20.2.75',
            'port': 1234,
            'ip_config': {
            'target_id': '',
            'target_pwd': '',
            'market_type': '',
            'resend_port': 1,
            'gw': 1,
            'i2': 1,},},],
            'work_time': '00:00:00|23:59:59',
            'target_max': 100,
            'node_number': 2,
            'send_bytes': 2,
            'update_time': 1577160228,
            'last_time_lag': 1577160228,
            'status': 'WARN',
            'res_monitor': {
            'cpu_transit': '',
            'memory_transit': '',
            'process_transit': '',
            'cpu_server': '',
            'memory_server': '',
            'process_server': '',
            'cpu_client': '',
            'memory_client': '',
            'process_client': '',},
            'write_block': '',
            'last_recv_file': '',
            'last_recv_time': '',
            'last_send_file': '',
            'last_send_time': '',
            'send_files': [{
            'market_type': '港交所行情',
            'group': 0,
            'enable': 0,
            'dir': 0,
            'recursive': 0,
            'path': 'C:\HGInfo\HGHQ.DBF',
            'filter_by_fn': '',
            'event_trigger': 0,
            'time_check': 0,
            'checksum_func': 'block',
            'scan': 200,
            'compress': 4,
            'filter_by_ft': '0|0',
            'work_time': '00-00-00|23-59-59',
            'play': 0,},],
            'recv_files': [{
            'market_type': '港交所行情',
            'path': '',
            'timeout': 0,
            'chk_tm_am': '09-00-00|11-30-00',
            'chk_tm_pm': '13-00-00|15-30-00',
            'record': 0,
            'group': 1,
            'enable': 0,
            'guard': 0,
            'watch': 0,},],
            'send_status': [{
            'market_type': 'xxxx',
            'file_name': '',
            'file_size': 0,
            'update_time': 1577160228,
            'send_bytes': 0,},],
            'recv_status': [{
            'market_type': 'xxxx',
            'file_name': '',
            'file_size': 0,
            'update_time': 1577160228,
            'send_bytes': 0,},],
            'recv_package': 1,
            'send_package': 1,
            'send_speed': 1,
            'recv_bytes': 1,
            'recv_bytes_last': 1,
            'protocol': '',
            'version_id': '',
            'sender_id': '',
            'heart_beat': 1,
            'auth_enable': 1,
            'auth_id': '',
            'compress': 1,
            'warn_config': [{
            'market_type': '',
            'file_name': '',
            'warn_tick': 1,
            'error_tick': 1,
            'check_begin': '',
            'check_end': '',
            'check_begin_pm': '',
            'check_end_pm': '',
            'check_node_number': 1,
            'traffic_begin': '',
            'traffic_end': '',
            'traffic_begin_pm': '',
            'traffic_end_pm': '',
            'traffic_upper': '',
            'traffic_lower': '',
            'traffic_upper_pm': '',
            'traffic_lower_pm': '',
            'file_size': 1,
            'send_bytes': 1,
            'system_time': 1,
            'update_time': 1,
            'warn_level': '',},],
        }
        
        node = Node(a)
        r = node.readme(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'readme', body)

    def testRegister(self):
        a = Auth(username, pwd)
        body = {
            'common': {
            'node_uuid': '278D0E2C-2156-3F7F-D75F-2628E46F6B35',
            'node_name': 'node1',
            'node_version': '4.0-19110518',
            'log_day': 10,
            'os_type': 0,
            'group_uuid': '',
            'system_time': 1577160228,},
            'node_list': [{
            'node_type': 1,
            'node_role': 1,
            'node_addr': [{
            'ip': '172.20.2.75',
            'port': 1234,},],
            'parent_addr': [{
            'ip': '172.20.2.75',
            'port': 1234,
            'ip_config': {
            'target_id': '',
            'target_pwd': '',
            'market_type': '6666',
            'resend_port': -1,
            'gw': 1,
            'i2': 0,},},],
            'work_time': '00:00:00|23:59:59',
            'target_max': 100,
            'write_block': '',
            'send_files': [{
            'market_type': '港交所行情',
            'group': 0,
            'enable': 0,
            'dir': 0,
            'recursive': 0,
            'path': 'C:\HGInfo\HGHQ.DBF',
            'filter_by_fn': '',
            'event_trigger': 0,
            'time_check': 0,
            'checksum_func': 'block',
            'scan': 200,
            'compress': 4,
            'filter_by_ft': '0|0',
            'work_time': '00-00-00|23-59-59',
            'play': 0,},],
            'recv_files': [{
            'market_type': '港交所行情',
            'path': '',
            'timeout': 0,
            'chk_tm_am': '09-00-00|11-30-00',
            'chk_tm_pm': '13-00-00|15-30-00',
            'record': 0,
            'group': 1,
            'enable': 0,
            'guard': 0,
            'watch': 0,},],
            'protocol': 'binary',
            'version_id': '1.01',
            'sender_id': '0',
            'heart_beat': 10,
            'auth_enable': 0,
            'auth_id': '0',
            'compress': 0,},],
        }
        
        node = Node(a)
        r = node.register(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'register', body)

    def testUpdateStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_type': 1,
            'node_version': '4.0-19110518',
            'system_time': 1577160228,
            'last_time_lag': 1577160228,
            'node_number': 2,
            'send_bytes': 317146,
            'res_monitor': {
            'cpu_transit': '0%',
            'memory_transit': '8032KB',
            'process_transit': 0,
            'cpu_server': '0%',
            'memory_server': '7448KB',
            'process_server': 0,
            'cpu_client': '0%',
            'memory_client': '0KB',
            'process_client': 0,},
            'last_recv_file': 'E:\test3\namelst-2019-01-28_05-07-28',
            'last_recv_time': 1577160221,
            'last_send_file': 'E:\test3\namelst-2019-01-28_05-07-28',
            'last_send_time': 1577160219,
            'send_status': [{
            'market_type': '港交所行情',
            'file_name': 'C:\\HGInfo\\HGXXN.DBF',
            'file_size': 123,
            'update_time': 1577160228,
            'send_bytes': 3567,},],
            'recv_status': [{
            'market_type': '港交所行情',
            'file_name': 'C:\\HGInfo\\HGXXN.DBF',
            'file_size': 123,
            'update_time': 1577160228,
            'send_bytes': 3567,},],
            'recv_package': 2,
            'send_package': 3,
            'send_speed': 4,
            'recv_bytes': 5,
            'recv_bytes_last': 6,
            'topography': {
            'node_uuid': '278D0E2C-2156-3F7F-D75F-2628E46F6B35',
            'byte_receive': 0,
            'byte_send': 47040,
            'consume': 0,
            'current_seq': 0,
            'current_time': '20201111222222556',
            'market_time': '20201111222222664',
            'last_market_time': '20201111222222664',
            'last_seq': 0,
            'pkt_receive': 34306,
            'pkt_send': 0,
            'node_list': [{
            'byte_send': 0,
            'ip': '172.20.2.76',
            'port': 41438,
            'speed': 3,
            'target_id': '66661111',
            'node_uuid': '',},],},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.updateStatus(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'updateStatus', body)

    def testListNode(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'node_type': 1,
            'node_role': 1,
            'status': '',
        }
        
        node = Node(a)
        r = node.listNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNode', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            'AEfB73F2-0d3b-BeC9-b7A3-fC2cF3e3cf7B',],
            'node_type': 1,
        }
        
        node = Node(a)
        r = node.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeStatus', body)

    def testDescribeNode(self):
        a = Auth(username, pwd)
        body = {
            'node_type': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.describeNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'describeNode', body)

    def testFileConfig(self):
        a = Auth(username, pwd)
        body = {
            'send_files': [{
            'market_type': '港交所行情',
            'group': 0,
            'enable': 0,
            'dir': 0,
            'recursive': 0,
            'path': 'C:\HGInfo\HGHQ.DBF',
            'filter_by_fn': '',
            'event_trigger': 0,
            'time_check': 0,
            'checksum_func': 'block',
            'scan': 200,
            'compress': 4,
            'filter_by_ft': '0|0',
            'work_time': '00-00-00|23-59-59',
            'play': 0,},],
            'recv_files': [{
            'market_type': '港交所行情',
            'path': '',
            'timeout': 0,
            'chk_tm_am': '09-00-00|11-30-00',
            'chk_tm_pm': '13-00-00|15-30-00',
            'record': 0,
            'group': 1,
            'enable': 0,
            'guard': 0,
            'watch': 0,},],
            'random_str': '',
            'node_role': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.fileConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'fileConfig', body)

    def testWarnConfig(self):
        a = Auth(username, pwd)
        body = {
            'node_type': '',
            'random_str': '',
            'warn_config': [{
            'market_type': '',
            'file_name': '',
            'warn_tick': 1,
            'error_tick': 1,
            'check_begin': '',
            'check_end': '',
            'check_begin_pm': '',
            'check_end_pm': '',
            'check_node_number': 1,
            'traffic_begin': '',
            'traffic_end': '',
            'traffic_begin_pm': '',
            'traffic_end_pm': '',
            'traffic_upper': '',
            'traffic_lower': '',
            'traffic_upper_pm': '',
            'traffic_lower_pm': '',},],
            'node_role': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.warnConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'warnConfig', body)

    def testUpgrade(self):
        a = Auth(username, pwd)
        body = {
            'upgrade_type': 1,
            'node_type': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.upgrade(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'upgrade', body)

    def testDelete(self):
        a = Auth(username, pwd)
        body = {
            'node_type': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        node = Node(a)
        r = node.delete(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'delete', body)

    def testTopography(self):
        a = Auth(username, pwd)
        body = {
            'is_static': 1,
            'node_uuid': '',
        }
        
        node = Node(a)
        r = node.topography(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'topography', body)

    def testLatency(self):
        a = Auth(username, pwd)
        body = {
            'start': 1,
            'end': 1,
            'type': '',
        }
        
        node = Node(a)
        r = node.latency(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'latency', body)


if __name__ == '__main__':
    unittest.main()
