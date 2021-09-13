from flask import Flask
from linebot import LineBotApi, WebhookHandler
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
if line_bot_api is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if handler is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)


# 將分散在資料夾的程式碼呼叫進來
from app import routes, models_for_line
