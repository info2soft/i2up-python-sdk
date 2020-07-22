from info2soft import config
from info2soft import https


class TimingRecovery(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     * 1 恢复 准备-2 恢复 获取还原时间点 - Mssql
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTimingRecoveryDb2Time(self, body):

        url = '{0}/timing/recovery/rc_db2_time'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-2 恢复 获取还原时间点 - Mssql
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTimingRecoveryMssqlTime(self, body):

        url = '{0}/timing/recovery/rc_mssql_time'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-3 恢复 获取Mssql初始信息
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def describeTimingRecoveryMssqlInitInfo(self, body):

        url = '{0}/timing/recovery/rc_mssql_init_info'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-1 恢复 获取还原时间点 - 文件
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTimingRecoveryPathList(self, body):

        url = '{0}/timing/recovery/rc_path_list'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-4 恢复 认证MsSql数据库
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def verifyTimingRecoveryMssqlInfo(self, body):

        url = '{0}/timing/recovery/rc_verify_mssql_info'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 --------------------------
     * 
     * @return array
     '''

    '''
     * 2 恢复 新建/编辑-1 恢复 新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createTimingRecovery(self, body):

        url = '{0}/timing/recovery'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 恢复 新建/编辑-3 恢复 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyTimingRecovery(self, body):

        url = '{0}/timing/recovery/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        randomStr = https._get(url, None, self.auth)[0]['data']['timing_recovery']['random_str']
        body['timing_recovery']['random_str'] = randomStr
        res = https._put(url, body, self.auth)
        return res

    '''
     * 2 恢复 新建/编辑-2 恢复 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeTimingRecovery(self, body):
        if body is None or 'task_uuid' not in body:
            exit()
        url = '{0}/timing/recovery/{1}'.format(config.get_default('default_api_host'), body['task_uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     * 3 恢复 列表-1 恢复 获取列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTimingRecovery(self, body):

        url = '{0}/timing/recovery'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-2 恢复 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTimingRecoveryStatus(self, body):

        url = '{0}/timing/recovery/status'.format(config.get_default('default_api_host'))
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-3 恢复 删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteTimingRecovery(self, body):

        url = '{0}/timing/recovery'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-4 恢复 操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def startTimingRecovery(self, body):

        url = '{0}/timing/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def stopTimingRecovery(self, body):

        url = '{0}/timing/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res
