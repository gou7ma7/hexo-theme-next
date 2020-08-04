# MySQL clinet局域网访问 mysqld
1. （使用docker启动）这个没啥说的，直接docker run 一把过，唯一注意的就是如果宿主机上在已经启动过mysqld了，那么docker run -p的端口号就要换一个了；ps: 密码是通过docker run  -e MYSQL_ROOT='pwd'启动的时候传环境变量设置的；
2. （我就是要练习自己搭建，咋说）：按照教程里面进入>mysql，也创建用户update user set user.Host='%' where user.User='root'; 本机连接是没有问题的，但是另一台机器client局域网登录的时候就报61 "Connection refused"；
3. 之前在公司里面都是叫网管然后秒解决，现在要自力更生了。
4. 首先再另一台机器client里面乱输入一个ip地址，报错为"Unknown MySQL server host"，不同于之前的被拒绝连接，说明当前host是ok，使用netstat -apn | grep 3306，看到tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      1016/mysqld         绑定到127.0.0.1，也就是回环了；
5. 目前既然知道是由于网络没有走通，那肯定就是配置的问题了，我找到mysql的配置文件，其中关于当前mysql用的是哪个配置文件里面有很多种说法，我不愿意深究，改成功的是/etc/mysql/mysql.conf.d/mysqld.cnf里边的bind-address;
6. 之后连接提示为1698 - Access denied for user 'root'@'IP'，说明现在的问题是密码设置的问题，大概要做的就是在启动的时候或者配置文件里面弄好连接密码，到时候client连接对口供就ok，我这边用在局域网又只玩就直接空密码了，反正以后也不会去没有网管的公司。 ps: 实际的默认密码在配置文件 /etc/mysql/debian.cnf 里面。


# 局域网ssh延迟非常严重的问题
1. 首先考虑ping该ip，如果出现丢包严重延迟正常就重启路由器，不能解决再排查；
2. 上诉不能解决或延迟≥100ms，考虑被ARP攻击、有人蹭网or下片、操作系统层面or物理设备问题等；

# ssh ubuntu 无法使用root账户登陆问题
改ssh本身的配置文件  
sshd服务的配置文件默认在/etc/ssh/sshd_config，正确调整相关配置项，可以进一步提高sshd远程登录的安全性。

配置文件的内容可以分为以下三个部分：

1. 常见SSH服务器监听的选项如下：

Port 22 //监听的端口为22

Protocol 2 //使用SSH V2协议

ListenAdderss 0.0.0.0 //监听的地址为所有地址

UseDNS no //禁止DNS反向解析

2. 常见用户登录控制选项如下：

PermitRootLogin no //禁止root用户登录

PermitEmptyPasswords no //禁止空密码用户登录

LoginGraceTime 2m //登录验证时间为2分钟

MaxAuthTries 6 //最大重试次数为6

AllowUsers user //只允许user用户登录，与DenyUsers选项相反

3. 常见登录验证方式如下：

PasswordAuthentication yes //启用密码验证

PubkeyAuthentication yes //启用秘钥验证

AuthorsizedKeysFile .ssh/authorized_keys //指定公钥数据库文件

# 在ssh 终端找不到环境变量的问题
问题描述：按照教程apt-get 之后手动在添加到profile文件之后依旧Command 'node' not found

1. 注意自己当前的登录账户，我之前不是root，~/ 出来的肯定就只能自己享受了

2. 具体那个配置文件不要改错了， 教材上面都是默认root账户来教你，我当时登录上去根本没有这个文件（因为以前没用root搞过  

3. 教程上面的版本可能不一样，直接复制添加到文件里面可能因为版本不同所以文件名不同，导致添加失败


各个配置文件区别如下：

> ~/.bashrc和 ~/.bash_profile,  \~/.profile 用于各个用户，这里的\~符号就是各当前用户的$HOME

> ~/.bash_profile 和 ~/.profile 只在登陆时读取一次。

> ~/.bashrc 每次都读取
