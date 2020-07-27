
from info2soft import config
from info2soft import https


class CloudBackup (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     *  准备 - 工作机获取设备列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listDevice(self, body):
        
        url = '{0}/cloud/ecs/device_info'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createBackup(self, body):
        
        url = '{0}/cloud/backup'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     *  修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def modifyCloudBackup(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/cloud/backup/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, None, self.auth)
        return res

    '''
     *  删除
     * 
     * @return list
    '''
    def deleteCloudBackup(self, ):
        
        url = '{0}/cloud/backup'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, None, self.auth)
        return res

    '''
     *  列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listCloudBackup(self, body):
        
        url = '{0}/cloud/backup'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  启动停止
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def operateCloudBackup(self, body):
        
        url = '{0}/cloud/backup'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  单个 
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeBackup(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/cloud/backup/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res
