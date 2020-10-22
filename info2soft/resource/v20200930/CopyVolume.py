
from info2soft import config
from info2soft import https


class CopyVolume (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 复制卷 - 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createCopyVolume(self, body):
        
        url = '{0}/copy_volume'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 复制卷 - 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def modifyCopyVolume(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/copy_volume/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._put(url, None, self.auth)
        return res

    '''
     * 复制卷 - 单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeCopyVolume(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/copy_volume/{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 复制卷 - 列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def copyVolumeList(self, body):
        
        url = '{0}/copy_volume'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 复制卷 - 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteCopyVolume(self, body):
        
        url = '{0}/copy_volume'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 获取单个卷快照列表
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def listSnapshotList(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/copy_volume//snapshot_list{1}'.format(config.get_default('default_api_host'), uuid)
        
        res = https._get(url, None, self.auth)
        return res

