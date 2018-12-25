
from info2soft import config
from info2soft import https


class FspMove (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 获取两节点网卡列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listFspMoveNic(self, body):
        
        url = '{0}/fsp/move/nic_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取源节点磁盘和文件列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listFspMoveDir(self, body):
        
        url = '{0}/fsp/move/dir_list'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 检测迁移条件-license
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def verifyFspMoveLicense(self, body):
        
        url = '{0}/fsp/move/verify_license'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 检测迁移条件-旧规则
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def verifyFspMoveOldRule(self, body):
        
        url = '{0}/fsp/move/verify_old_rule'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 检测迁移条件-磁盘
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def verifyFspMoveVolumeSpace(self, body):
        
        url = '{0}/fsp/move/verify_volume_space'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 检测迁移条件-系统版本
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def verifyFspMoveOsVersion(self, body):
        
        url = '{0}/fsp/move/verify_os_version'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 新建规则
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def createFspMove(self, body):
        
        url = '{0}/fsp/move'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改规则
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyFspMove(self, body):
        
        url = '{0}/reg:/fsp/move/[a-f0-9-] '.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 获取单个规则
     * 
     * @return array
     '''
    def describeFspMove(self, ):
        
        url = '{0}/reg:/fsp/move/[a-f0-9-] '.format(config.get_default('default_api_host'))
        
        res = 
        return res

    '''
     * 删除规则
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def deleteFspMove(self, body):
        
        url = '{0}/fsp/move'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取规则列表（基本信息）
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listFspMove(self, body):
        
        url = '{0}/fsp/move'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 规则操作
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def startFspMove(self, body):
        
        url = '{0}/fsp/move/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 规则状态
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listFspMoveStatus(self, body):
        
        url = '{0}/fsp/move/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

