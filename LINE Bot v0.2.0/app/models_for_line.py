from app import handler
from app import line_bot_api, handler

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import random

@handler.add(MessageEvent, message=TextMessage)
def message_text_echo(event):
    
    message_text = event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_text)
    )
