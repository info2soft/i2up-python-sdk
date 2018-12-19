# -*- coding: utf-8 -*-

# from info2soft import zone

API_HOST = 'http://192.168.25.101:58080/api'  # 数据处理操作Host

# _BLOCK_SIZE = 1024 * 1024 * 4  # 断点续上传分块大小，该参数为接口规格，暂不支持修改

_config = {
    'default_api_host': API_HOST,
    'connection_timeout': 30,        # 链接超时为时间为30s
    'connection_retries': 3,         # 链接重试次数为3次
    'connection_pool': 10,           # 链接池个数为10
}


def get_default(key):
    return _config[key]


def set_default(
        connection_retries=None, connection_pool=None,
        connection_timeout=None, default_api_host=None):
    if default_api_host:
        _config['default_api_host'] = default_api_host
    if connection_retries:
        _config['connection_retries'] = connection_retries
    if connection_pool:
        _config['connection_pool'] = connection_pool
    if connection_timeout:
        _config['connection_timeout'] = connection_timeout
