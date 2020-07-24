
from info2soft import config
from info2soft import https


class Db (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 数据库列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listDbs(self, body):
        
        url = '{0}/active/db'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 修改数据库节点
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyDb(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/active/db/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 测试数据库连接
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def checkDbLink(self, body):
        
        url = '{0}/active/db/db_check'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 新建数据库节点
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createDb(self, body):
        
        url = '{0}/active/db'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 删除数据库
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteDb(self, body):
        
        url = '{0}/active/db'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 数据库状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listDbStatus(self, body):
        
        url = '{0}/active/db/status'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 数据库健康信息
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def describeDbHealthInfo(self, body):
        
        url = '{0}/active/db/health_info'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 表空间查询接口
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def describeDbSpace(self, body):
        
        url = '{0}/active/db/space_query'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取单个数据库节点信息
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeDb(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/active/db/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 批量导入下载模板
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def importTemplate(self, body):
        
        url = '{0}/dl'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 批量导入
     * 
     * @return list
    '''
    def batchCreateDbs(self, body):
        
        url = '{0}/active/db/batch'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

