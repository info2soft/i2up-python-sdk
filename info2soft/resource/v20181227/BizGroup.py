
from info2soft import config
from info2soft import https


class BizGroup (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 1 添加
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createBizGroup(self, body):
        
        url = '{0}/biz_grp'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 更新
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modifyBizGroup(self, body):
        
        url = '{0}/biz_grp/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 3 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeBizGroup(self, body):
        if body is None or 'uuid' not in body:
           exit()
        url = '{0}/biz_grp/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 5 删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteBizGroup(self, body):
        
        url = '{0}/biz_grp'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 4 获取列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listBizGroup(self, body):
        
        url = '{0}/biz_grp'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 更新绑定
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def updateBizGroupBind(self, body):
        
        url = '{0}/biz_grp/{1}/bind'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 2 获取绑定情况
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def listBizGroupBind(self, body):
        if body is None or 'uuid' not in body:
           exit()
        url = '{0}/biz_grp/{1}/bind'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 1 获取 Res 列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listBizGroupResource(self, body):
        
        url = '{0}/biz_grp/res'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

