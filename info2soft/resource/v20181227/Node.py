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
        rsa = Rsa()
        osPwd = rsa.rsaEncrypt(body['os_pwd'])
        body.update({'os_pwd': osPwd})
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

        url = '{0}/node/{1}'.format(config.get_default('default_api_host'), body['node']['node_uuid'])
        rsa = Rsa()
        osPwd = rsa.rsaEncrypt(body['node']['os_pwd'])
        body['node'].update({'os_pwd': osPwd})
        randomStr = https._get(url, None, self.auth)[0]['data']['node']['random_str']
        body['node']['random_str'] = randomStr
        res = https._put(url, body, self.auth)
        return res

    '''
     * 获取单个节点
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''

    def describeNode(self, body):
        if body is None or 'node_uuid' not in body:
            exit()
        url = '{0}/node/{1}'.format(config.get_default('default_api_host'), body['node_uuid'])

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
        if body is None or 'node_uuid' not in body:
            exit()
        url = '{0}/node/{1}/device_info'.format(config.get_default('default_api_host'), body['node_uuid'])

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
        if body is not None:
            for k, v in body.items():
                # 如果包含了数组形式的数据需要处理一下 url
                if isinstance(body[k], list):
                    urlEnd = '&node_uuids[]='
                    url = url + '?node_uuids[]=' + urlEnd.join(body[k])
        res = https._get(url, None, self.auth)
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



