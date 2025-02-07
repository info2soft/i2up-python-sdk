
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Notifications
from info2soft.common.v20250123.Notifications import Notifications
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


class NotificationsTestCase(unittest.TestCase):

    def testUpdateNotifyConf(self):
        a = Auth(username, pwd)
        body = {
            'stop_alerts': 1,
            'audio_alert_notify': 1,
            'single_alert_loop_broadcast_times': 1,
            'custom_audio': '',
            'notify_contact_biz': {
            'phone': '11111111111',
            'email': 'test@info2sost.com',},
            'notify_contact_chk': {
            'phone': '11111111111',
            'email': 'test@info2sost.com',
            'policy': {
            'every': 'month',
            'days': '5,6',},},
            'notify_contact_status': {
            'phone': '11111111111',
            'email': 'test@info2sost.com',
            'policy': {
            'every': 'hour',
            'gap': '4',},},
            'sms_id': '',
            'wechat_id': '',
            'notify_limit': '10',
            'normal_notify_switch': 0,
            'alarm_shield': {
            'type': {
            'node': False,
            'db': False,
            'rule': False,
            'task': False,},
            'level': {
            'info': False,
            'warn': False,
            'report': False,
            'err': False,
            'fatal': False,
            'recover': False,},
            'code': '',},
            'alarm_config': {
            'alarm_interval': 1,
            'max_analyze_halt_tm': 1,
            'max_delay': 1,
            'max_err_table_num': 1,
            'max_err_dml_num': 1,
            'max_err_ddl_num': 1,
            'max_cpu': '',
            'max_mem': '',
            'max_net': '',
            'max_disk': '',
            'max_alarm_interval': '',
            'max_load_halt_tm': '',
            'max_analyze_delay': '',
            'max_cpu_delay_alarm_time': '',
            'max_mem_delay_alarm_time': '',
            'max_net_delay_alarm_time': '',
            'max_disk_delay_alarm_time': '',
            'max_analyze_halt_tm_alarm_time': '',
            'max_analyze_delay_alarm_time': '',
            'max_delay_alarm_time': '',
            'max_load_halt_tm_alarm_time': '',
            'max_cpu_delay_unit': '',
            'max_mem_delay_unit': '',
            'max_net_delay_unit': '',
            'max_disk_delay_unit': '',
            'max_analyze_halt_tm_unit': '',
            'max_analyze_delay_unit': '',
            'max_load_halt_tm_unit': '',
            'max_delay_unit': '',
            'max_cpu_delay_duration': '',
            'max_mem_delay_duration': '',
            'max_net_delay_duration': '',
            'max_disk_delay_duration': '',
            'max_analyze_halt_tm_duration': '',
            'max_analyze_delay_duration': '',
            'max_load_halt_tm_duration': '',
            'max_delay_duration': '',
            'max_cpu_delay_duration_unit': '',
            'max_mem_delay_duration_unit': '',
            'max_net_delay_duration_unit': '',
            'max_disk_delay_duration_unit': '',
            'max_analyze_halt_tm_duration_unit': '',
            'max_analyze_delay_duration_unit': '',
            'max_load_halt_tm_duration_unit': '',
            'max_delay_duration_unit': '',},
            'notify_limit_type': '',
            'alarm_level_map': {
            'info': '',
            'warn': '',
            'report': '',
            'err': '',
            'fatal': '',
            'recover': '',},
        }
        
        
        notifications = Notifications(a)
        r = notifications.updateNotifyConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'updateNotifyConf', body)

    def testListNotifyConf(self):
        a = Auth(username, pwd)
        body = {
            'keys': [
            'notify_limit',
            'normal_notify_switch',
            'notify_contact_biz',
            'notify_contact_chk',
            'notify_contact_status',
            'sms_id',
            'wechat_id',
            'stop_alerts',
            'alarm_shield',
            'alarm_config',
            'custom_audio',
            'single_alert_loop_broadcast_times',
            'audio_alert_notify',],
        }
        
        
        notifications = Notifications(a)
        r = notifications.listNotifyConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'listNotifyConf', body)

    def testAddNotifications(self):
        a = Auth(username, pwd)
        body = {
            'type': 'timing',
            'uuid': '82275AFD-97D0-15B4-D477-011E397113D6',
            'msg': '规则/任务执行失败/成功/超时/策略取消',
            'name': 'timing_test',
            'cc_uuid': '',
            'resume_normal': 1,
        }
        
        
        notifications = Notifications(a)
        r = notifications.addNotifications(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'addNotifications', body)

    def testListNotifications(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'order_by': 'status',
            'direction': 'ASC',
            'lic_alert': 0,
            'where_args': {
            'status': 1,
            'played': 1,},
        }
        
        
        notifications = Notifications(a)
        r = notifications.listNotifications(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'listNotifications', body)

    def testDescribeNotifications(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        notifications = Notifications(a)
        r = notifications.describeNotifications(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'describeNotifications', body)

    def testDescribeNotificationsCount(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        notifications = Notifications(a)
        r = notifications.describeNotificationsCount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'describeNotificationsCount', body)

    def testReadNotifications(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
            'type': 1,
        }
        
        
        notifications = Notifications(a)
        r = notifications.readNotifications(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'readNotifications', body)

    def testPlayNotifications(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
            'type': 1,
        }
        
        
        notifications = Notifications(a)
        r = notifications.playNotifications(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'playNotifications', body)

    def testDeleteNotifications(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        notifications = Notifications(a)
        r = notifications.deleteNotifications(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'deleteNotifications', body)

    def testDescribeNotificationsConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        notifications = Notifications(a)
        r = notifications.describeNotificationsConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'describeNotificationsConfig', body)

    def testUpdateNotificationsConfig(self):
        a = Auth(username, pwd)
        body = {
            'config': [{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},{
            'type': 1,
            'email_sw': 0,
            'sms_sw': 1,
            'p_sms_sw': 1,
            'sms_temp': '',
            'wechat_sw': 0,
            'maintenance_sw': 0,
            'principal': '',
            'webhook_sw': 0,
            'webhook_uuid': '',
            'content_temp_uuid': '',
            'kafka_sw': 0,
            'snmp_sw': 0,
            'notify_contact_user': {
            'email': '',
            'phone': '',},
            'real_sms_template': '',
            'sms_report_template': '',},],
        }
        
        
        notifications = Notifications(a)
        r = notifications.updateNotificationsConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'updateNotificationsConfig', body)

    def testTestNotificationsSms(self):
        a = Auth(username, pwd)
        body = {
            'temp_id': '',
            'mobile': '13123456789',
        }
        
        
        notifications = Notifications(a)
        r = notifications.testNotificationsSms(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'testNotificationsSms', body)

    def testTestNotificationsEmail(self):
        a = Auth(username, pwd)
        body = {
            'email': 'lis@info2soft.com',
        }
        
        
        notifications = Notifications(a)
        r = notifications.testNotificationsEmail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'testNotificationsEmail', body)

    def testResetNotificationsTimes(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        notifications = Notifications(a)
        r = notifications.resetNotificationsTimes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'resetNotificationsTimes', body)

    def testListEmailTemplate(self):
        a = Auth(username, pwd)
        body = {
            'direction': 'ASC',
            'type': '',
        }
        
        
        notifications = Notifications(a)
        r = notifications.listEmailTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'listEmailTemplate', body)

    def testModifyEmailTemplate(self):
        a = Auth(username, pwd)
        body = {
            'content': '',
            'comment': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        notifications = Notifications(a)
        r = notifications.modifyEmailTemplate(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'modifyEmailTemplate', body)


if __name__ == '__main__':
    unittest.main()
