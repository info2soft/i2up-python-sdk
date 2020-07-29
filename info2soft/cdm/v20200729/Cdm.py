
from info2soft import config
from info2soft import https


class Cdm (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 备份点列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getPointList(self, body):
        
        url = '{0}/cdm/point_full_info_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取资源列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getResourceList(self, body):
        
        url = '{0}/cdm/drp_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取主机存储资源
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getHostStorageList(self, body):
        
        url = '{0}/cdm/host_storage_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * -- 列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def takeOverDrillList(self, body):
        
        url = '{0}/cdm_rule'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * -- 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createTakeOverDrill(self, body):
        
        url = '{0}/cdm_rule'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * -- 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteTakeOverDrill(self, body):
        
        url = '{0}/cdm_rule'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * -- 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeTakeOverDrill(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/cdm_rule/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * -- 获取虚机状态
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def getVmStatus(self, body):
        
        url = '{0}/cdm_rule/vm_status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * -- 操作
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def operateTakeOverDrill(self, body):
        
        url = '{0}/cdm_rule/operate'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

