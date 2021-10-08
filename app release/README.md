# app release
###### tags: `Linebot` `Python`
此版本的內容透過將Linebot app功能獨立出來，這樣的架構有助閱讀與擴充：

```
flie:.
|    Procfile
|    core.py
|    config.ini
|    requirements.txt
|    runtime.txt
|    
-----app
    |    __init__.py
    |    routes.py
    |    models_for_line.py
```
1. core.py  
> Linebot核心用以啟用Linebot，此版本的Linebot寫法將app功能獨立於`core.py`中，較容易修改與擴充。  

2. Procfile  
> Heroku平台的執行文件`web: gunicorn file_name.py:app --preload`，告訴Heroku的Dyno要執行什麼檔案。  

3. config.ini  
> 作為儲存有關於APP's config的內容，Heroku平台上副檔名必須是`.ini`，如Token等重要資料可以寫在config避免在同一個`.py`檔揭露。  

4. requirements.txt  
> 向Dyno請求我們需要的套件，使其安裝我們指定的套件來建構運行環境，可以指定版本：`line-bot-sdk==1.20.0`。

5. runtime.txt  
> 告訴Heroku要用什麼版本的`python`來運行Linebot：`python-3.8.12`，如果沒有指定，Heroku會自動使用較穩定的版本。  

6. app資料夾
> 將所有api放置在app中，容易辨識與整理擴充，利用python class做整理，容易修正bug。

7. `__init__.py`
> 初始化我們的機器人與後端，然後呼叫並執行app中的程式碼。

8. models_for_line.py
> Linebot的功能主要放置在這個`.py`中，使用`@handler`作為linebot api的管理。

9. routes.py
> route是flask後端app使用的語法，我們將flask建立在此，最主要的功能是建立與Line平台做webhook與註冊我們Bot的後端，再者也可以增加網頁內容來介紹自己的Linebot，或是串連金流平台等等。
