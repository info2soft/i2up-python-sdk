from info2soft import config
from info2soft import https


class VirtualizationSupport(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     *  新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createVp(self, body):

        url = '{0}/vp/platform'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVp(self, body):
        if body is None or 'vp_uuid' not in body: exit()
        url = '{0}/vp/platform/{1}'.format(config.get_default('default_api_host'), body['vp_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  编辑
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyVp(self, body):

        url = '{0}/vp/platform/{1}'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     *  列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVp(self, body):

        url = '{0}/vp/platform'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpStatus(self, body):

        url = '{0}/vp/platform/status'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteVp(self, body):

        url = '{0}/vp/platform'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     *  查询 虚机列表
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVM(self, body):

        url = '{0}/vp/platform/{1}/vm'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 平台属性
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpAttribute(self, body):
        if body is None or 'vp_uuid' not in body: exit()
        url = '{0}/vp/platform/{1}/info'.format(config.get_default('default_api_host'), body['vp_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  查询 备机上备份列表（RC）1
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listBakVer(self, body):

        url = '{0}/vp/platform/{1}/bak_ver'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 备份点信息/虚机配置信息（RC）2
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listBakVerInfo(self, body):

        url = '{0}/vp/platform/{1}/bak_ver_info'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 数据存储下文件列表（RC）3
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listDatastoreFile(self, body):

        url = '{0}/vp/platform/{1}/datastore_file'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 数据中心列表（MOVE/REP）1
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def listDatacenter(self, body):
        if body is None or 'vp_uuid' not in body: exit()
        url = '{0}/vp/platform/{1}/datacenter'.format(config.get_default('default_api_host'), body['vp_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  操作
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''

    def updateDataAgentVp(self, body):

        url = '{0}/vp/platform/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  查询 数据中心主机列表 （MOVE/REP）2
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listDatacenterHost(self, body):

        url = '{0}/vp/platform/{1}/datacenter_host'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 存储列表 （MOVE/REP）3
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listDatastore(self, body):

        url = '{0}/vp/platform/{1}/datastore'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     *  查询 存储信息 （MOVE/REP）4
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listDatastoreInfo(self, body):

        url = '{0}/vp/platform/{1}/datastore_info'.format(config.get_default('default_api_host'), body['vp_uuid'])
        del body['vp_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 ----------------------------
     * 
     '''

    '''
     *  新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createVpBackup(self, body):

        url = '{0}/vp/backup'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  修改（仅模板）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyVpBackup(self, body):

        url = '{0}/vp/backup/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])
        del body['rule_uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     *  获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpBackup(self, body):
        if body is None or 'rule_uuid' not in body: exit()
        url = '{0}/vp/backup/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  获取单个（组）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpBackupGroup(self, body):
        if body is None or 'group_uuid' not in body: exit()
        url = '{0}/vp/backup/{1}/group'.format(config.get_default('default_api_host'), body['group_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpBackup(self, body):

        url = '{0}/vp/backup'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  列表（组）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpBackupGroup(self, body):

        url = '{0}/vp/backup/group'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpBackupStatus(self, body):

        url = '{0}/vp/backup/status'.format(config.get_default('default_api_host'))
        res = https._get(url, body, self.auth)
        return res

    '''
     *  操作 启停
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def startVpBackup(self, body):

        url = '{0}/vp/backup/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  操作 启停
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def stopVpBackup(self, body):

        url = '{0}/vp/backup/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteVpBackup(self, body):

        url = '{0}/vp/backup'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 ----------------------------
     * 
     '''

    '''
     *  新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createVpRecovery(self, body):

        url = '{0}/vp/recovery'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  获取单个（组）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpRecoveryGroup(self, body):
        if body is None or 'group_uuid' not in body: exit()
        url = '{0}/vp/recovery/{1}/group'.format(config.get_default('default_api_host'), body['group_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  获取列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpRecovery(self, body):

        url = '{0}/vp/recovery'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpRecoveryStatus(self, body):

        url = '{0}/vp/recovery/status'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  操作 启停
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def startVpRecovery(self, body):

        url = '{0}/vp/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def stopVpRecovery(self, body):

        url = '{0}/vp/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def clearFinishVpRecovery(self, body):

        url = '{0}/vp/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *   删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteVpRecovery(self, body):

        url = '{0}/vp/recovery'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 ----------------------------
     * 
     '''

    '''
     *  新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createVpMove(self, body):

        url = '{0}/vp/move'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpMove(self, body):
        if body is None or 'rule_uuid' not in body: exit()
        url = '{0}/vp/move/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  修改（模板）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyVpMove(self, body):

        url = '{0}/vp/move/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])
        del body['rule_uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     *  获取列表
     * 
     * @return array
     '''

    def listVpMove(self, body):

        url = '{0}/vp/move'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpMoveStatus(self, body):

        url = '{0}/vp/move/status'.format(config.get_default('default_api_host'))
        res = https._get(url, body, self.auth)
        return res

    '''
     *  操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def stopVpMove(self, body):

        url = '{0}/vp/move/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def startVpMove(self, body):

        url = '{0}/vp/move/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def moveVpMove(self, body):

        url = '{0}/vp/move/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteVpMove(self, body):

        url = '{0}/vp/move'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     *  新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createVpRep(self, body):

        url = '{0}/vp/rep'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeVpRep(self, body):
        if body is None or 'rule_uuid' not in body: exit()
        url = '{0}/vp/rep/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  修改（模板）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyVpRep(self, body):

        url = '{0}/vp/rep/{1}'.format(config.get_default('default_api_host'), body['rule_uuid'])
        del body['rule_uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     *  获取列表
     * 
     * @return array
     '''

    def listVpRep(self, body):

        url = '{0}/vp/rep'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVpRepStatus(self, body):

        url = '{0}/vp/rep/status'.format(config.get_default('default_api_host'))
        res = https._get(url, body, self.auth)
        return res

    '''
     *  操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def stopVpRep(self, body):

        url = '{0}/vp/rep/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def startVpRep(self, body):

        url = '{0}/vp/rep/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def failoverVpRep(self, body):

        url = '{0}/vp/rep/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def failbackVpRep(self, body):

        url = '{0}/vp/rep/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteVpRep(self, body):

        url = '{0}/vp/rep'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     *  获取快照列表信息
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def listVpRepPointList(self, body):
        if body is None or 'rule_uuid' not in body: exit()
        url = '{0}/vp/rep/{1}/point_list'.format(config.get_default('default_api_host'), body['rule_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  文件恢复 - 1 获取恢复虚机ip
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def describeVpFileRecoveryVmIp(self, body):

        url = '{0}/vp/file_recovery/vm_ip'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  文件恢复 - 2 livecd磁盘分区
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def vpFileRecoveryLivecdPartition(self, body):

        url = '{0}/vp/file_recovery/livecd_partition'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  文件恢复 - 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def createVpFileRecovery(self, body):

        url = '{0}/vp/file_recovery'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  文件恢复 - 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
     '''
    def describeVpFileRecovery(self, body):
        if body is None or 'uuid' not in body: exit()
        url = '{0}/vp/file_recovery/{1}'.format(config.get_default('default_api_host'), body['uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     *  文件恢复 - 获取列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def listVpFileRecovery(self, body):

        url = '{0}/vp/file_recovery'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  文件恢复 - 状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def listVpFileRecoveryStatus(self, body):

        url = '{0}/vp/file_recovery/status'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     *  文件恢复 - 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def deleteVpFileRecovery(self, body):

        url = '{0}/vp/file_recovery'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

