from info2soft import config
from info2soft import https


class Db(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     * 同步规则列表
     * 
     * @return list
    '''

    def listDbRule(self, ):

        url = '{0}/db2/rule'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res

    '''
     * 新建规则
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''

    def createDbRule(self, body):

        url = '{0}/db2/rule'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改规则
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''

    def modifyDbRule(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/db2/rule/{1}'.format(config.get_default('default_api_host'), uuid)

        res = https._put(url, None, self.auth)
        return res

    '''
     * 单条规则
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''

    def describeDbRule(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/db2/rule/{1}'.format(config.get_default('default_api_host'), uuid)

        res = https._get(url, None, self.auth)
        return res

    '''
     * 删除规则
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''

    def deleteDbRule(self, body):

        url = '{0}/db2/rule'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * 日志
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''

    def listDbRuleLog(self, body):

        url = '{0}/db2/rule/log'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

