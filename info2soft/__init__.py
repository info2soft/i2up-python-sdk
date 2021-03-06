# -*- coding: utf-8 -*-
'''
    info2soft Resource Storage SDK for Python
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    For detailed document, please see:
    <https://code.info2soft.com/web/sdk/python-sdk>
'''

# flake8: noqa

__version__ = 'v20181227'

from .config import set_default


from info2soft.common.Auth import Auth, RequestsAuth
from info2soft.common.DataBaseBackup import DataBaseBackup
from info2soft.common.Dir import Dir
from info2soft.common.GeneralInterface import GeneralInterface
from info2soft.common.Logs import Logs
from info2soft.common.Monitor import Monitor
from info2soft.common.Permission import Permission
from info2soft.common.Qr import Qr
from info2soft.common.Storage import Storage


from info2soft.dashboard.v20181227.Dashboard import Dashboard


from info2soft.fsp.v20181227.FspRecovery import FspRecovery
from info2soft.fsp.v20181227.FspBackup import FspBackup
from info2soft.fsp.v20181227.FspMove import FspMove


from info2soft.ha.v20181227.AppHighAvailability import AppHighAvailability


from info2soft.nas.v20190102.NAS import NAS


from info2soft.notifications.v20181227.Notifications import Notifications


from .rep.v20181227.RepBackup import RepBackup
from .rep.v20181227.RepRecovery import RepRecovery


from .resource.v20181227.Node import Node
from .resource.v20181227.Cluster import Cluster
from .resource.v20181227.BizGroup import BizGroup


from .system.v20181227.User import User
from .system.v20181227.Lic import Lic
from .system.v20181227.Settings import Settings


from .timing.v20181227.TimingBackup import TimingBackup
from .timing.v20181227.TimingRecovery import TimingRecovery


from .tools.v20181227.Compare import Compare
from .tools.v20181227.Diagnose import Diagnose


from .vp.v20181227.VirtualizationSupport import VirtualizationSupport

from .active.v20200720.SyncRules import SyncRules

