
from info2soft import config
from info2soft import https


class DtoStorage (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 存储 - 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createDtoStorage(self, body):
        
        url = '{0}/dto/storage'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 存储 - 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyDtoStorage(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/dto/storage/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 存储 - 单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeDtoStorage(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/dto/storage/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 存储 - 列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listDtoStorage(self, body):
        
        url = '{0}/dto/storage'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 存储 - 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteDtoStorage(self, body):
        
        url = '{0}/dto/storage'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

