
from info2soft import config
from info2soft import https


class RepBackup (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 新建规则
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createRepBackup(self, body):
        
        url = '{0}/rep/backup'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 获取单个规则
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeRepBackup(self, body):
        if body is None or 'uuid' not in body:
            exit()
        url = '{0}/rep/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 修改规则
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modifyRepBackup(self, body):
        
        url = '{0}/rep/backup/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        print(url)
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 删除规则
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteRepBackup(self, body):
        
        url = '{0}/rep/backup'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 规则操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startRepBackup(self, body):
        
        url = '{0}/rep/backup/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    def stopRepBackup(self, body):

        url = '{0}/rep/backup/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 规则状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepBackupStatus(self, body):
        
        url = '{0}/rep/backup/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取规则列表（基本信息）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepBackup(self, body):
        
        url = '{0}/rep/backup'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * cdp baseline 列表 获取
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepBackupBaseLine(self, body):
        
        url = '{0}/rep/backup//cdp_bl_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * cdp baseline 列表 删除
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteRepBackupBaseline(self, body):
        
        url = '{0}/rep/backup//cdp_bl_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 孤儿文件 列表 获取
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepBackupOrphan(self, body):
        
        url = '{0}/rep/backup//orphan_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * 孤儿文件 列表 删除
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteRepBackupOrphan(self, body):
        
        url = '{0}/rep/backup//orphan_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 孤儿文件 下载
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def downloadRepBackupOrphan(self, body):
        
        url = '{0}/rep/backup//orphan_download{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * 快照 列表 获取
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepBackupSnapshot(self, body):
        
        url = '{0}/rep/backup//snapshot_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * 快照 列表 创建快照
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def createRepBackupSnapshot(self, body):
        if body is None or 'uuid' not in body:
            exit()
        url = '{0}/rep/backup//snapshot_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._post(url, None, self.auth)
        return res

    '''
     * 快照 列表 删除
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteRepBackupSnapshot(self, body):
        
        url = '{0}/rep/backup//snapshot_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._delete(url, body, self.auth)
        return res

    '''
     *  获取规则列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def repBackup(self, body):
        
        url = '{0}/dashboard/rep'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

