
from info2soft import config
from info2soft import https


class StoragePool (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 新建存储池
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createStoragePool(self, body):
        
        url = '{0}/storage_pool'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改存储池
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyStoragePool(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/storage_pool/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 查看列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def storagePoolList(self, body):
        
        url = '{0}/storage_pool'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeStoragePool(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/storage_pool/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteStoragePool(self, body):
        
        url = '{0}/storage_pool'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listStoragePoolStatus(self, body):
        
        url = '{0}/storage_pool/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

