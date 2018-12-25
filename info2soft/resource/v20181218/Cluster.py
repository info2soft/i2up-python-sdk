from info2soft import config
from info2soft import https


class Cluster(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     * 1 集群认证
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def authCls(self, body):
        url = '{0}/cls/auth'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 集群节点验证
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def verifyClsNode(self, body):
        url = '{0}/cls/node_verify'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 新建集群
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def createCls(self, body):
        url = '{0}/cls'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 获取单个集群
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeCls(self, body):
        if body is None or body.has_key('uuid'):
            pass
        url = '{0}/cls/{1}'.format(config.get_default('default_api_host'), body['uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     * 3 修改集群
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def modifyCls(self, body):
        url = '{0}/cls/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 1 获取集群列表（基本信息）
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def listCls(self, body):
        url = '{0}/cls'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 2 集群状态
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def listClsStatus(self, body):
        url = '{0}/cls/status'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 3 删除集群
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def deleteCls(self, body):
        url = '{0}/cls'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * 4 集群操作
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''

    def clsDetail(self, body):
        url = '{0}/cls/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

