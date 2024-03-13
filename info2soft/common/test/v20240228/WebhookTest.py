
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.Webhook import Webhook
# from info2soft.common.v20200722.Webhook import Webhook
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


class WebhookTestCase(unittest.TestCase):

    def testCreateWebhook(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'name': '',
            'type': '',
            'url': '',
        }
        
        webhook = Webhook(a)
        r = webhook.createWebhook(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'createWebhook', body)

    def testModifyWebhook(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'random_str': '',
            'config': {},
            'url': '',
            'id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        webhook = Webhook(a)
        r = webhook.modifyWebhook(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'modifyWebhook', body)

    def testListWebhook(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1
        }
        
        webhook = Webhook(a)
        r = webhook.listWebhook(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'listWebhook', body)

    def testDescribeWebhook(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        webhook = Webhook(a)
        r = webhook.describeWebhook(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'describeWebhook', body)

    def testDeleteWebhook(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        webhook = Webhook(a)
        r = webhook.deleteWebhook(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'deleteWebhook', body)

    def testCreateWebhookContentTemplate(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'warn_type': '',
            'id': '',
        }
        
        webhook = Webhook(a)
        r = webhook.createWebhookContentTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'createWebhookContentTemplate', body)

    def testModifyWebhookContentTemplate(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'name': '',
            'warn_type': '',
            'webhook_type': '',
            'random_str': ''
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        webhook = Webhook(a)
        r = webhook.modifyWebhookContentTemplate(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'modifyWebhookContentTemplate', body)

    def testListWebhookContentTemplate(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'limit': 1,
            'page': 1
        }
        
        webhook = Webhook(a)
        r = webhook.listWebhookContentTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'listWebhookContentTemplate', body)

    def testDelteWebhookContentTemplate(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        webhook = Webhook(a)
        r = webhook.delteWebhookContentTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Webhook', 'delteWebhookContentTemplate', body)


if __name__ == '__main__':
    unittest.main()
