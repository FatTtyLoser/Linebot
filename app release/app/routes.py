from app import app, handler
from flask import (
    request, render_template, redirect, url_for, flash
)
from linebot.exceptions import (
    InvalidSignatureError
)

# 接收 LINE 平台送來的「通知」
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
