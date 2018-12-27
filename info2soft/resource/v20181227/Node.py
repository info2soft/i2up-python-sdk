from info2soft import config
from info2soft import https
from info2soft.common.Rsa import Rsa


class Node(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     * 新建节点
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def authNode(self, body):
        url = '{0}/node/auth'.format(config.get_default('default_api_host'))
        Rsas = Rsa()
        print(body)
        osPwd = Rsas.encrypt(body['os_pwd'])
        print(osPwd)
        body.update({'os_pwd': osPwd})
        print(body)
        res = https._post(url, body, self.auth)
        return res

    '''
     * 获取节点容量
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def checkCapacity(self, body):

        url = '{0}/node/check_capacity'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取节点卷组列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listVg(self, body):

        url = '{0}/node/vg'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 检查节点在线
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def checkNodeOnline(self, body):

        url = '{0}/node/hello'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 新建节点
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createNode(self, body):

        url = '{0}/node'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改节点
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyNode(self, body):

        url = '{0}/node/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._put(url, body, self.auth)
        return res

    '''
     * 获取单个节点
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeNode(self, body):
        if body is None or 'uuid' not in body:
            exit()
        url = '{0}/node/{1}'.format(config.get_default('default_api_host'), body['uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     * 新建节点 - 批量
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def createBatchNode(self, body):

        url = '{0}/node/batch'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 获取节点存储信息
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeDeviceInfo(self, body):
        if body is None or 'uuid' not in body:
            exit()
        url = '{0}/node//device_info{1}'.format(config.get_default('default_api_host'), body['uuid'])

        res = https._get(url, None, self.auth)
        return res

    '''
     * 获取节点列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listNode(self, body):

        url = '{0}/node'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 节点操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def upgradeNode(self, body):

        url = '{0}/node/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 节点状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listNodeStatus(self, body):

        url = '{0}/node/status'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 删除节点
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def deleteNode(self, body):

        url = '{0}/node'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     *  获取节点列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def node(self, body):

        url = '{0}/dashboard/node'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

