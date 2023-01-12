# Telegram 收发微信消息 - Docker compose 一键部署【2023最新版】

github 地址：https://github.com/zhangyile/telegram-wechat.git

efb项目的原理是这样的：  
Telegram bot > EFB > 微信网页版 > 微信

使用 itchat-uos 替换了 itchat
* itchat-uos: https://github.com/why2lyj/ItChat-UOS
* itchat: https://github.com/littlecodersh/ItChat

## 0. 环境依赖
- 一个正常使用的 Telegram 账号
- 一个正常使用的微信号 （微信号需实名并绑有银行卡，否则无法登录 UOS 网页版微信）
- docker / docker compose （本文以 docker compose 为例，怎么安装，自己网上找教程）
- 一台 Linux 服务器 （需与 api.telegram.org 能通信）

## 1.  Telegram 上创建机器人并获取 Token 和 ID
### 1.1获取 Bot Token
1. 在 Telegram 里, 对 @botfather 说话: /newbot
2. 按照要求给 Bot 取名
3. 获取 Bot Token安全原因: Token 必须保密（这串token要记好，待会要用）
4. 允许 Bot 读取非指令信息，对 @botfather 说话: /setprivacy, 选择disable
5. 允许将 Bot 添加进群组，对 @botfather 说话: /setjoingroups, 选择enable
6. 允许 Bot 提供指令列表，对 @botfather 说话: /setcommands, 输入以下内容 （复制以下内容一次性发给botfather）
```
help - 显示命令列表.
link - 将远程会话绑定到 Telegram 群组
chat - 生成会话头
recog - 回复语音消息以进行识别
info - 显示当前 Telegram 聊天的信息.
unlink_all - 将所有远程会话从 Telegram 群组解绑.
update_info - 更新群组名称和头像
extra - 获取更多功能
```


### 1.2 获取 Telegram 账户 ID
再和另外一个机器人 @get_id_bot 对话（也是搜索得到这个机器人），点击 start 即可获得你的 Telegram ID，一串数字（Chat ID）。

至此，Telegram 的配置完成，我们得到两个重要的数字：token、Telegram ID（待会要用）


## 2. 部署服务

```
# 拉取仓库代码
git clone https://github.com/zhangyile/telegram-wechat.git

# 修改 config.py 文件，填入 Token 和 ID
cd telegram-wechat && vi config.py

# 启动服务
docker compose up -d 

# 查看日志中的微信二维码，扫码登录
docker compose logs -f

```


## 3. 开始使用
> 原文：https://specialhua.top/20190618/cid=4.html

首先在 Telegram 中创建一个新的群组，比如 哈哈哈呵呵呵 这个名字，然后将你的机器人邀请进来（此处，手机端的 Telegram 无法直接拉机器人进来，你需要随便拉一个真人，再拉机器人进来，再把那个人踢出去；电脑端则可以在创建群组的时候直接拉机器人进来）

回到你的机器人对话中，如果你要将一个叫“哈哈哈呵呵呵”的微信好友单独作为TG中的聊天对话框，你就输入 /link 哈哈哈（不必输全名，机器人会检索含有此关键字的所有好友，然后选择link，选择你刚刚创建的 哈哈哈呵呵呵 这个群组，成功后，以后这个叫哈哈哈呵呵呵 的好友发来的信息不会在机器人那显示了，而是在这个群组）

我把常聊的几个人单独建了TG群，使消息分流，其余不常用的，使用机器人窗口接收，公众号及群消息也单独建群。



## 4. 我都做了什么改动？
### 4.1 修改了 `eh_wechat_slave.py` 文件
因为 itchat-uos 源码里移除了 itchat 的 new_instance 方法。此处改为使用  itchat-uos 的 load_sync_itchat 方法。 
```
......
 125         #self.itchat = itchat.new_instance()
 126         self.itchat = itchat.load_sync_itchat()
 ......
```

### 4.2 基础镜像安装了 ffmpeg-linux64-v3.3.1
因为 royx/docker-efb 镜像里没有 ffmpeg ，每次启动，都要去下载。



## 5. 参考链接
- https://specialhua.top/20190618/cid=4.html
- https://www.iszy.cc/posts/ehforwarderbot/

