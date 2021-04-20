import requests
from bs4 import BeautifulSoup
import simplejson as json

req = requests.get('https://republika.co.id/')

obj = BeautifulSoup(req.text,"html.parser")

print("----Menampilkan Semua Teks Headline----")
print("=======================================")


file = open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    file.write(headline.find('h2').text)
    file.write('\n')
file.close()

file = open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\headline.txt','r')
for f in file:
    print(f)
file.close()

data = []
f = open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\headline.json','w')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    data.append({"judul":headline.find('h2').text})
jdump = json.dumps(data)
f.writelines(jdump)
f.close()
