# ssh ubuntu 无法使用root账户登陆问题
改ssh本身的配置文件  
sshd服务的配置文件默认在/etc/ssh/sshd_config，正确调整相关配置项，可以进一步提高sshd远程登录的安全性。

配置文件的内容可以分为以下三个部分：

1、常见SSH服务器监听的选项如下：

Port 22 //监听的端口为22

Protocol 2 //使用SSH V2协议

ListenAdderss 0.0.0.0 //监听的地址为所有地址

UseDNS no //禁止DNS反向解析

2、常见用户登录控制选项如下：

PermitRootLogin no //禁止root用户登录

PermitEmptyPasswords no //禁止空密码用户登录

LoginGraceTime 2m //登录验证时间为2分钟

MaxAuthTries 6 //最大重试次数为6

AllowUsers user //只允许user用户登录，与DenyUsers选项相反

3、常见登录验证方式如下：

PasswordAuthentication yes //启用密码验证

PubkeyAuthentication yes //启用秘钥验证

AuthorsizedKeysFile .ssh/authorized_keys //指定公钥数据库文件
