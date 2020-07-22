
from info2soft import config
from info2soft import https


class Mask (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 敏感类型列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listTypes(self, body):
        
        url = '{0}/mask/sens_type'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 新建脱敏算法
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createAlgo(self, body):
        
        url = '{0}/mask/newalgo'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 脱敏算法列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listAlgos(self, body):
        
        url = '{0}/mask/algo'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 脱敏规则列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listMaskRules(self, body):
        
        url = '{0}/mask/rule'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 新建脱敏规则
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createMaskRules(self, body):
        
        url = '{0}/mask/rule'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 删除规则
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteMaskRule(self, body):
        
        url = '{0}/mask/rule'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listMaskRuleStatus(self, body):
        
        url = '{0}/mask/rule/status'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 集合列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listMap(self, body):
        
        url = '{0}/mask/sens_map'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 新建集合
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createMap(self, body):
        
        url = '{0}/mask/sens_map'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改集合
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyMap(self, body):
        
        url = '{0}/mask/sens_map/:id'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 删除集合
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteMap(self, body):
        
        url = '{0}/mask/sens_map'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取单个集合
     * 
     * @return list
    '''
    def descriptMap(self, ):
        
        url = '{0}/mask/sens_map/:id'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 新建数据库集合
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createDbMap(self, body):
        
        url = '{0}/mask/sens_db_map'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 数据库集合列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listDbMap(self, body):
        
        url = '{0}/mask/sens_db_map'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 删除数据库集合
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteDbMap(self, body):
        
        url = '{0}/mask/sens_db_map'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 修改数据库集合
     * 
     * @return list
    '''
    def modifyDbMap(self, ):
        
        url = '{0}/mask/sens_db_map'.format(config.get_default('default_api_host'))
        
        res = https._put(url, None, self.auth)
        return res

    '''
     * 新建敏感发现任务
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createSensCheck(self, body):
        
        url = '{0}/mask/sens_check'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改敏感发现任务
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifySensCheck(self, body):
        
        url = '{0}/mask/sens_check/:uuid'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 删除敏感发现任务
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteSensCheck(self, body):
        
        url = '{0}/mask/sens_check/delete'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取敏感发现列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listSensCheck(self, body):
        
        url = '{0}/mask/sens_check'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取单个任务详情
     * 
     * @return list
    '''
    def descriptSensCheck(self, ):
        
        url = '{0}/mask/sens_check/:uuid'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

