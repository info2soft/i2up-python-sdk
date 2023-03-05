
from info2soft import config
from info2soft import https


class Npsvr (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * npsvr - 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createNpsvr(self, body):
        
        url = '{0}/vp/npsvr'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * npsvr - 认证
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def authNpsvr(self, body):
        
        url = '{0}/vp/npsvr/auth'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * npsvr - 列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listNpsvr(self, body):
        
        url = '{0}/vp/npsvr'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * npsvr - 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyNpsvr(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/vp/npsvr/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * npsvr - 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteNpsvr(self, body):
        
        url = '{0}/vp/npsvr'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * npsvr - 状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getNpsvrStatus(self, body):
        
        url = '{0}/vp/npsvr/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * npsvr - 维护模式修改
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def switchNpsvrMaintenance(self, body):
        
        url = '{0}/vp/npsvr/maintenance'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

