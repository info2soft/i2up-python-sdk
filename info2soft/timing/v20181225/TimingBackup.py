
from info2soft import config
from info2soft import https


class TimingBackup (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 1 备份 准备-4 备份 获取MsSql数据源
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def describeTimingBackupMssqlSource(self, body):
        
        url = '{0}/timing/backup/mssql_source'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-1 备份/恢复 认证Oracle信息（目前未使用）
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def verifyTimingBackupOracleInfo(self, body):
        
        url = '{0}/timing/backup/verify_oracle_info'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-2 备份/恢复 获取Oracle表空间（目前未使用）
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def describeTimingBackupOracleContent(self, body):
        
        url = '{0}/timing/backup/oracle_content'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-3 备份 获取Oracle脚本路径
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def descibeTimingBackupOracleSriptPath(self, body):
        
        url = '{0}/timing/backup/oracle_script_path'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-5 备份 获取MsSql数据库列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingBackupMssqlDbList(self, body):
        
        url = '{0}/timing/backup/mssql_db_list'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 --------------------------
     * 
     * @return array
     '''
    # def tempFuncName(self, ):
    #
    #     url = '{0}/dash_timing_1'.format(config.get_default('default_api_host'))
    #
    #     res =
    #     return res

    '''
     * 2 备份 新建/编辑-1 备份 新建
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def createTimingBackup(self, body):
        
        url = '{0}/timing/backup'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 备份 新建/编辑-2 备份 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeTimingBackup(self, body):
        if body is None or body.has_key('uuid'):
                         pass
        url = '{0}/timing/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 2 备份 新建/编辑-3 备份 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyTimingBackup(self, body):
        
        url = '{0}/timing/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-1 备份 获取列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingBackup(self, body):
        
        url = '{0}/timing/backup'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-2 备份 状态
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingBackupStatus(self, body):
        
        url = '{0}/timing/backup/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-3 备份 删除
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def deleteTimingBackup(self, body):
        
        url = '{0}/timing/backup'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-4 备份 操作
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/timing/backup/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * ------------------------- 分隔线 --------------------------
     * 
     * @return array
     '''
    # def tempFuncName(self, ):
    #
    #     url = '{0}/dash_timing_2'.format(config.get_default('default_api_host'))
    #
    #     res =
    #     return res

    '''
     * 1 恢复 准备-2 恢复 获取还原时间点 - Mssql
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingRecoveryMssqlTime(self, body):
        
        url = '{0}/timing/recovery/rc_mssql_time'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-3 恢复 获取Mssql初始信息
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def describeTimingRecoveryMssqlInitInfo(self, body):
        
        url = '{0}/timing/recovery/rc_mssql_init_info'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-1 恢复 获取还原时间点 - 文件
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingRecoveryPathList(self, body):
        
        url = '{0}/timing/recovery/rc_path_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 恢复 准备-4 恢复 认证MsSql数据库
     * 
     * @param array $body  参数详见 API 手册
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
    # def tempFuncName(self, ):
    #
    #     url = '{0}/dash_timing_3'.format(config.get_default('default_api_host'))
    #
    #     res =
    #     return res

    '''
     * 2 恢复 新建/编辑-1 恢复 新建
     * 
     * @param array $body  参数详见 API 手册
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
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyTimingRecovery(self, body):
        
        url = '{0}/timing/recovery/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 2 恢复 新建/编辑-2 恢复 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeTimingRecovery(self, body):
        if body is None or body.has_key('uuid'):
                         pass
        url = '{0}/timing/recovery/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 3 恢复 列表-1 恢复 获取列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingRecovery(self, body):
        
        url = '{0}/timing/recovery'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-2 恢复 状态
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listTimingRecoveryStatus(self, body):
        
        url = '{0}/timing/recovery/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-3 恢复 删除
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def deleteTimingRecovery(self, body):
        
        url = '{0}/timing/recovery'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 3 恢复 列表-4 恢复 操作
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/timing/recovery/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 策略 新建
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/policy'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 策略 获取单个
     * 
     * @return array
     '''
    # def tempFuncName(self, ):
    #
    #     url = '{0}/reg:/policy/[a-f0-9-] '.format(config.get_default('default_api_host'))
    #
    #     res =
    #     return res

    '''
     * 3 策略 修改
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/reg:/policy/[a-f0-9-] '.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 1 策略 获取列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/policy'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 策略 删除
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/policy'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 4 策略 操作
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/policy/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

