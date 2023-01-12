master_channel = 'plugins.eh_telegram_master', 'TelegramChannel'
slave_channels = [('plugins.eh_wechat_slave', 'WeChatChannel')]

eh_telegram_master = {
    "token": "xxxxxxxxxxxxxxxxx", # YOUR_TELEGRAM_BOT_TOKEN
    "admins": [1234567890],       # YOUR_TELEGRAM_ID
    "bing_speech_api": ["xxx", "xxx"],
    "baidu_speech_api": {
        "app_id": 0,
        "api_key": "xxx",
        "secret_key": "xxx"
    }
}
