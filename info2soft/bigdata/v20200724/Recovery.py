
from info2soft import config
from info2soft import https


class Recovery (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     *  准备 - 获取备份列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listBackupHistory(self, body):
        
        url = '{0}/bigdata/recovery/bak_history'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createBigdataRecovery(self, body):
        
        url = '{0}/bigdata/recovery'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     *  单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeBigdataRecovery(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/bigdata/recovery/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteBigdataRecovery(self, body):
        
        url = '{0}/bigdata/recovery'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     *  列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listBigdataRecovery(self, body):
        
        url = '{0}/bigdata/recovery'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listBigdataRecoveryStatus(self, body):
        
        url = '{0}/bigdata/recovery/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  操作
     * 
     * @body 参考 API 文档
     * @return 
    '''
    def operateBigdataRecovery(self, body):
        url = '{0}/bigdata/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     *  认证
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def authBigdataPlatform(self, body):
        
        url = '{0}/bigdata/backup/auth'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

