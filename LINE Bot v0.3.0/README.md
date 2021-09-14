# 套件應用過程

`import urllib`
由於 urllib 是內建函數，所以只需要 import 函數。
```
url = "http://www.google.com/"
變數A = urllib.request.urlopen(url)
print(conn)
```
宣告 url 的網址為何後，利用 urlopen 打開網址，print出結果為：
```
<http.client.HTTPResponse object at 0x000001B68F910A00>
```
```
data = 變數A.read()
print(data)
```
透過 `變數A.read()` 即可以得到網頁的原始碼，與透過瀏覽器開啟網頁後檢視原始碼內容一樣。

最後是利用 urllib 套件的使用與帶入 Header 假以瀏覽器的身分提供伺服器辨識後，可獲得 html 的內容，也是網路爬蟲的第一步：
```
url = "http://google.com/"
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

req = urllib.request.Request(url,headers=hearders)
conn = urllib.request.urlopen(req)

data = conn.read()
print(data)
```

接著由於 LINE Bot 回傳的 image 訊息只能透過網頁，所以我們將搜尋 google 圖片，來做自動化回傳給 LINE 用戶。

假設：
`search_url='https://www.google.com/search?q=%E8%99%8E%E6%96%91%E8%B2%93&sxsrf=AOaemvLvaXzC4hmqOyZCRsNSKmH4h25LnA:1631324959155&source=lnms&tbm=isch&sa=X&ved=2ahUKEwishdCF5_XyAhU0zIsBHRRbDM8Q_AUoAXoECAEQAw&biw=1920&bih=937'`

透過 python split 功能：
`search_url.split('&')`

得到：
```
['https://www.google.com/search?q=%E8%99%8E%E6%96%91%E8%B2%93',
 'sxsrf=AOaemvLvaXzC4hmqOyZCRsNSKmH4h25LnA:1631324959155',
 'source=lnms',
 'tbm=isch',
 'sa=X',
 'ved=2ahUKEwishdCF5_XyAhU0zIsBHRRbDM8Q_AUoAXoECAEQAw',
 'biw=1920',
 'bih=937']
```
1. 第一行顯示出 google 搜尋的結果，設定 q 代指我們用來搜尋的關鍵字(query)
2. 第二行代表我們正在發送搜尋請求的瀏覽器種類。
3. 第三NO
4. 第四行不知，isch就是image search的縮寫。
5. 第五NO
6. 第六NO
7. 第七行是螢幕的寬度(width)
8. 第八行是螢幕的高度(height)

小結：得知我們要使用goole搜尋，只要輸入：
`'https://www.google.com/search?tbm=usch&q=關鍵字'`

另一種解析網址的方式，透過 urllib 套件。
```
u = urllib.parse.urlparse(search_url)
print(u)
```
得到
```
ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', 
query='q=%E8%99%8E%E6%96%91%E8%B2%93&sxsrf=AOaemvLvaXzC4hmqOyZCRsNSKmH4h25LnA:1631324959155&source=lnms&tbm=isch&sa=X&ved=2ahUKEwishdCF5_XyAhU0zIsBHRRbDM8Q_AUoAXoECAEQAw&biw=1920&bih=937', fragment='')
```
或者使用 `urllib.parse.parse_qs(u[4])` 得到：
```
{'q': ['虎斑貓'],
 'sxsrf': ['AOaemvLvaXzC4hmqOyZCRsNSKmH4h25LnA:1631324959155'],
 'source': ['lnms'],
 'tbm': ['isch'],
 'sa': ['X'],
 'ved': ['2ahUKEwishdCF5_XyAhU0zIsBHRRbDM8Q_AUoAXoECAEQAw'],
 'biw': ['1920'],
 'bih': ['937']}
```
就可以獲得清楚的搜尋網址的解析，反向操作則是：
```
search_image= {'tbm': 'isch' , 'q' : '虎斑貓'}
urllib.parse.urlencode(search_image)
```
得到了：`'tbm=isch&q=%E8%99%8E%E6%96%91%E8%B2%93'
`與解析網址的結果相仿，也就是 google 看得懂的編碼。

小結
```
search_image= {'tbm': 'isch' , 'q' : '虎斑貓'}
url = f"http://www.google.com/search?{urllib.parse.urlencode(search_image)}/"
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

req = urllib.request.Request(url,headers=headers)
conn = urllib.request.urlopen(req)

data = conn.read()
print(data)
```
`https://www.google.com.tw/search?tbm=isch&q=%E8%99%8E%E6%96%91%E8%B2%93`
由此可見，我們只要將 ==q== 的部分作為變數，就可以在這一步解析網址，假如 google 搜尋圖片的網頁架構不變，我們將可以利用爬蟲技巧，一次將搜尋結果的多張圖片擷取出網址，並且由於 LINE 平台的 image message 回應只能透過網址，並有容量限制，所以剛好可以這樣做出自動化。

接著將搜尋頁面的網址透過 F12 開發者工具，可以將搜尋圖片的網頁結構抓出有規律者，透過爬蟲一次爬取下來：
```
pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
image_list = []

q_string = {'tbm':'isch', 'q': event.message.text}
url = f"https://www.google.com/search?{urllib.parse.urlencode(q_string)}/"
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
req = urllib.request.Request(url,headers=headers)
conn = urllib.request.urlopen(req)

pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
image_list = []

for match in re.finditer(pattern, str(data, 'utf-8')):
    image_list.append(re.sub(r'\\u003d','=',match.group(1)))
    
random_img_url = img_list[random.randint(0, len(img_list)+1)]

line_bot_api.reply_message(
    event.reply_token,
    ImageSendMessage(
        original_content_url = random_img_url,
        preview_image_url = random_img_url
    )
)
```
以上的書本範例包含一些網路爬蟲的技術與 line_bot_api 的使用，假如使用 request 套件可能可以更好理解，做為下一個版本的修改目標。

參考資料：LINE Bot by Python 全攻略：從Heroku到AWS跨平台實踐（iT邦幫忙鐵人賽系列書） -作者： 饒孟桓  
