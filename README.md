

## info2soft SDK for Python

## 运行环境

| info2soft SDK版本 | Python 版本 |
|:---------------:|:---------------------------:|
|       9.x       |          3.x|

---

## 安装方式

通过 `pip` 安装

> 如果网络不好，可以使用清华大学镜像源，命令如下：

```bash
$ pip install somePackage -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

> 如果提示pip版本较低，请升级pip，命令如下：

```bash
$ python3 -m pip install --upgrade pip
```
## 方式1：直接安装SDK及所有依赖
```
$ pip install i2up-Python-SDK
```
## 方式2：获取SDK源码包，手动安装依赖

```bash
$ pip install requests

$ pip install simplejson

$ pip install pytest

$ pip install flake8

$ pip install rsa

$ pip install crypto pycryptodome

$ pip install pyopenssl

```

---

## 使用示例

###   配置入口文件 config.py

路径: /info2soft/config.py

配置 `API_HOST` 参数为你的控制机 IP 地址即可

    # API_HOST = 'https://127.0.0.1:58086/api'
    

###   运行时对配置文件进行自定义

> 可配置的参数可以参考 info2soft/config.py 的注释

比如修改默认 host
```

...
from info2soft import config

config.set_default(None, None, None, 'https://172.0.0.1:58086/api')
...

```

###  获取复制规则列表

保存为 xxx.py

    ...

    # -*- coding: utf-8 -*-
    # flake8: noqa
    
    import sys
    # SDK 代码包所在位置需要加入 path 中。
    sys.path.append(r'C:\python_sdk')
    from info2soft import RepBackup
    from info2soft import Auth
    
    # 2种方式创建 Auth 对象
    # 1. 使用用户名密码的方式创建 Auth 对象
    username = 'admin'
    pwd = 'Info1234'
    a = Auth(username, pwd)
    
    # 2. 使用 ak + sk 的方式创建 Auth 对象
    # ak = 'your ak' # 英方平台 Access Key
    # sk = 'your sk' # 英方平台 Secret Key
    # a = Auth('', '', 'ak', ak, sk)

    # 参考 API 文档，构造请求参数
    body = {
        'search_value': '',
        'limit': 1,
        'type': 1,
        'page': 1,
        'search_field': '',
    }
    repBackup = RepBackup(a)
    ret, info = repBackup.listRepBackup(body)
    if ret is not None:
        print('All is OK')
    else:
        print(info) # error message in info

    ...

###   执行脚本

```bash
$ python3 xxx.py
```

---

## 常见问题

- 上面的例子中第二个参数 info 保留了请求响应的信息，失败情况下 ret 为 none, 将 info 可以打印出来，提交给我们。
- API 的使用 demo 可以参考 [模块测试](https://gitee.com/i2soft/i2up-python-sdk/tree/v20250123/info2soft/resource/test)。
- 如果碰到`ImportError: No module named requests.auth` 请安装 `requests` 。


##  API 接口入参参考
- API 入参请参考 [API使用手册](https://docs.i2yun.com/i2up-docs/)。


## 代码贡献

详情参考[代码提交指南](CONTRIBUTING.md)。

## 联系我们

- 如果需要帮助，请联系邮箱: support@info2soft.com
- 如果发现了bug或功能需求， 欢迎提交 [issue](https://gitee.com/i2soft/i2up-python-sdk/issues)
- 如果要提交代码，欢迎提交 pull request


 
    
