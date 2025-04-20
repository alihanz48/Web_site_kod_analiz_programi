import requests
import json

url="https://youtube.com"

webdata=requests.get(url)
htmlcodes=str(webdata.content)

with open('html_tags.json',encoding="utf-8") as veri:
    tags=json.load(veri)

analiz=""
for tag in tags['tags']:
    adet=htmlcodes.count(str(tag['tag']))
    if adet!=0:
     analiz+=str(adet)+" adet "+tag['tag']+ " etiketi\n"

analiz+="kullanılmıştır."
print(analiz)