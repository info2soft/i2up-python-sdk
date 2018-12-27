# -*- coding: utf-8 -*-
'''
Qiniu Resource Storage SDK for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For detailed document, please see:
<https://code.info2soft.com/web/sdk/python-sdk>
'''

# flake8: noqa

__version__ = 'v20181227'

from info2soft.common.Auth import Auth, RequestsAuth

from .config import set_default

from .system.v20181227.User import User

from .resource.v20181227.Node import Node

from .resource.v20181227.Cluster import Cluster