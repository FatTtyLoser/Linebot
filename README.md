# **Linebot相關語法與資訊**
> [name=FatTtyLoser]
> [Gihub][https://github.com/FatTtyLoser]
###### tags `Linebot` `Python`
### **Chapter：**
* **Descript this repositories**  
* **LineBotApi**  
* **HerokuCLI**  
* **Git**  
* **Relevant information collation**  
---
## **Descript this repositories**



## **LineBotApi**


`line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World'))`  
回應從使用者推送過來的事件。  

`line_bot_api.push_message(to, TextSendMessage(text='XXXXXXX'))`  
主動向使用者推送訊息

`reply_message` 讓Line聊天機器人懂得有人說話要回覆，回覆則使用 `TextSendMessage` 寫成：

```python
image_message = ImageSendMessage(
	original_content_url=' ---網址--- ',
	preview_image_url=' ---網址--- '
)
```
Line聊天機器人回覆event(使用image)  
**LINE提供的ImageSendMessage是靠統一資源定位器(uniform resource licator\網址)**  

---
## **HerokuCLI**


`heroku login -i`  
登入 Heroku 帳號，( -i ) 從 cmd 連線。

`heroku create APP名稱`  
在當前 Heroku 帳號下，創建一個新的 Heroku 帳號下，創建一個新的 Heroku APP。

`heroku git:remote -a APP名稱`  
將指定的 Heroku APP 設定為 git 推送的遠端資料庫。

`heroku config`  
查詢當前Heroku APP的設定變數(config Vars)

`heroku config:add TZ="Asia/Taipei"`  
在當前的 Heroku APP 中新增一個鍵值配對(Key:Value)為TZ:"Asia/Taipei"的設定變數。

`heroku ps -a APP名稱`  
查詢 Heroku APP 的狀態資訊，可以看到免費時數的用量。

`heroku addons -a APP名稱`  
利用 addons 查詢掛載擴充元件， -a APP 是指定查詢的 dyno 。

`heroku addons:create heroku-postgresql: 選定方案名稱(free:hobby-dev)`  
創造資料庫進行掛載。

#### 查看日誌：

`heroku logs --app {Heroku app name} --tail`  
查看即時日誌，一小時未更新則退出即時狀態。

---
## **Git 常用指令**



`git --version` 查版本

`git init` 初始化當前的目錄，讓 Git 開始進行版本管理。

`git add .` 將當前目錄下的所有檔案加入到 Git 的版本管理索引中。

`git commit -m "註解"` 將放在索引的檔案提交成一個新的版本，並附上一些註解，通常會寫上辨識名稱甚至是email，同時記錄也可以進行修改。

---
## **Heroku 相關資訊**


- `python-3.9.7` on all [supported stacks](https://devcenter.heroku.com/articles/stack#stack-support-details)
- `python-3.8.12` on all [supported stacks](https://devcenter.heroku.com/articles/stack#stack-support-details)
- `python-3.7.12` on all [supported stacks](https://devcenter.heroku.com/articles/stack#stack-support-details)
- `python-3.6.15` on all [supported stacks](https://devcenter.heroku.com/articles/stack#stack-support-details)

---
## **Note**

* Heroku 所提供的資料庫是 Heroku Postgres ，屬於 PostgreSQL ，關聯式資料庫 (relational database) 的其中一種。

* SQL 結構化查詢語言 (structured query language) ，可以用來定義數據以及整理數據。

* Heroku Postgres 掛載在 dyno 下的擴充元件 (add-ons) 。一個 dyno 可以掛載多個料庫，而資料庫也可以連接到多個 dyno 。

* hobby-dev 免費方案。  

Line 接收並回傳到後端的 ==event== 完整內容：
```
{
  "message": {
    "id": "14754094388544",
    "text": "DWQDWQWDQKJLDJLQWKJD",
    "type": "text"
  },
  "mode": "active",
  "replyToken": "3e3203d5ce1545a1973259d1521e6a49",
  "source": {
    "type": "user",
    "userId": "U03ec69e0943e37a5d8937a7711404a87"
  },
  "timestamp": 1631757835147,
  "type": "message"
}
```

---
## **PostgreSQL**


