
from info2soft import config
from info2soft import https


class TimingBackup (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 1 备份 准备-4 备份 获取MsSql数据源
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeTimingBackupMssqlSource(self, body):
        
        url = '{0}/timing/backup/mssql_source'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-1 备份/恢复 认证Oracle信息（目前未使用）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def verifyTimingBackupOracleInfo(self, body):
        
        url = '{0}/timing/backup/verify_oracle_info'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-2 备份/恢复 获取Oracle表空间（目前未使用）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeTimingBackupOracleContent(self, body):
        
        url = '{0}/timing/backup/oracle_content'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-3 备份 获取Oracle脚本路径
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def descibeTimingBackupOracleSriptPath(self, body):
        
        url = '{0}/timing/backup/oracle_script_path'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 备份 准备-5 备份 获取MsSql数据库列表
     * 
     * @param dict body  参数详见 API 手册
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
     
     * 2 备份 新建/编辑-1 备份 新建
     * 
     * @param dict body  参数详见 API 手册
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
        if body is None or 'uuid' not in body:
            exit()
        url = '{0}/timing/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 2 备份 新建/编辑-3 备份 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modifyTimingBackup(self, body):
        
        url = '{0}/timing/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        randomStr = https._get(url, None, self.auth)[0]['data']['timing_backup']['random_str']
        body['timing_backup']['random_str'] = randomStr
        res = https._put(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-1 备份 获取列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listTimingBackup(self, body):
        
        url = '{0}/timing/backup'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-2 备份 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listTimingBackupStatus(self, body):
        
        url = '{0}/timing/backup/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-3 备份 删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteTimingBackup(self, body):
        
        url = '{0}/timing/backup'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 3 备份 列表-4 备份 操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startTimingBackup(self, body):
        
        url = '{0}/timing/backup/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    def stopTimingBackup(self, body):
        url = '{0}/timing/backup/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

