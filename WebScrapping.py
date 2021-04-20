# Import package requests dan BeautifulSoup
import requests
import simplejson
from bs4 import BeautifulSoup
from datetime import datetime

# Request ke Website
page = requests.get("https://www.republika.co.id/")

# Extract content to object
obj = BeautifulSoup(page.text,'html.parser')
data = []

# Extract Data From div class="bungkus_txt_headline"
terkini = obj.find_all('div',class_='conten1')
f=open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\data.json','w')
for article in terkini:
    title = article.find('h2').text
    category = article.find('h1').text
    publish = article.find('div',class_='date').text
    now = datetime.now()
    date = now.strftime("%d %B %Y %H:%M:%S")

    data.append({"title":title, "category":category, "publish":publish, "date":date})

print("JSON Updated")
jdumps = simplejson.dumps(data)
f.writelines(jdumps)
f.close()
