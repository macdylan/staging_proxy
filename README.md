Staging 切换
-----------
通过配合浏览器插件，实现应用级的代理切换，无需修改 hosts 或系统配置。

## Requirements

- FoxyProxy on Firefox
- Switchy on Chromium / Chrome

## Installation

- FoxyProxy
    - Firefox -> Tools -> Add-ons -> Get Add-ons -> Search: FoxyProxy
- Switchy
    - Chromium -> <https://chrome.google.com/webstore/category/home> -> Search: Proxy Switchy [from Mhd Hejazi]

## Setup

**PAC URL:** `http://bit.ly/QDALI7`


### 先以 FoxyProxy 为例说明：

1. 点击右上方狐狸头，弹出配置对话框，点击其中 Add New Proxy 按钮，出现以下界面

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s1.png)

    选择 Automatic Proxy Configuration by PAC，填入: `http://bit.ly/QDALI7`
    
2. 选择 General，填入 Proxy Name，这里以 JMStaging 为例

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s4.png)

3. 点击 OK 进行确认

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s5.png)

4. 右键点击右上方狐狸头，选择 JMStaging 配置即可

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s6.png)

### 以下为 Switchy 的配置说明：

1. 点击 Switchy 图标进入配置

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s7.png)
    点击左侧 New Profile，填入配置内容。配置方法于 FoxyProxy 类似。

2. 点击 Switchy 图标，选择 Profile

    ![](https://raw.github.com/macdylan/staging_proxy/master/img/s8.png)

### Safari on Mac 使用手册


    下载：
    https://nodeload.github.com/macdylan/staging_proxy/zipball/master

    或者通过源码：
    git clone git://github.com/macdylan/staging_proxy.git
    
进入 scripts 文件夹，找到 Switcher.app 拖到 Dock 上，执行后提示输入管理员密码。不用担心，这里没有任何文件操作，也没有后台进程，因为修改 WIFI 的代理配置，Apple 必须要求管理员授权。

第一次执行为启动，第二次执行为关闭。

目前还没有提供 Profile 供选择。如果使用有线连接，需修改以下：

    $ vim scripts/Switcher.app/Contents/Resources/switcher_for_mac
    DEVICE='Wi-Fi' # or Ethernet

