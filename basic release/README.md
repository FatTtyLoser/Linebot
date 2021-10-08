# Basic release
###### tags: `Linebot` `Python`
此版本的內容可以直接推送到Heroku服務平台上運行成功，最基本的架構誠如：

```
flie:.
    Procfile
    core.py
    config.ini
    requirements.txt
    runtime.txt
```
1. core.py  
> Linebot核心的python檔案，所有的功能都在這個.py中實現，載入所有的模組套件、建立flask後台接收LINE平台的回傳資訊、webhook到line devolope平台、載入linebot與handler使用token、最重要的註冊並啟用BOT。在這個版本之中，Linebot的功能必須都放在`.py`檔內。  

2. Procfile  
> Heroku平台的執行文件`web: gunicorn file_name.py:app --preload`，告訴Heroku的Dyno要執行什麼檔案。  

3. config.ini  
> 作為儲存有關於APP's config(配置)的內容，Heroku平台上副檔名必須是ini，如Token等重要資料可以寫在config避免在同一個.py檔揭露。  

4. requirements.txt  
> 向Dyno請求我們需要的套件，使其安裝我們指定的套件來建構運行環境，可以指定版本：`line-bot-sdk==1.20.0`。

5. runtime.txt  
> 告訴Heroku要用什麼版本的`python`來運行Linebot：`python-3.8.12`，如果沒有指定，Heroku會自動使用較穩定的版本。  
