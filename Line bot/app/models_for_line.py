from app import handler
from app import line_bot_api, handler

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import random
import re
import urllib

def google_isch(q_string):
    q_string= {'tbm': 'isch' , 'q' : q_string}
    url = f"http://www.google.com/search?{urllib.parse.urlencode(q_string)}/"
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }

    req = urllib.request.Request(url,headers=headers)
    conn = urllib.request.urlopen(req)

    data = conn.read()
    pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
    image_list = []

    for match in re.finditer(pattern, str(data, 'utf-8')):
        image_list.append(match.group(1))

    return image_list[2]

@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):

    if event.source.user_id != "FatTtyLoserfatfatFatTtyLoserfatty":

        try:
            image_url = google_isch(event.message.text)
            message_text = image_url
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url = image_url,
                    preview_image_url = image_url
                )
            )
        except:
            message_text = '小丑，淘汰！'
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=message_text)
            )
