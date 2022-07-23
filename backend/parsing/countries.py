# from cgitb import text
import json
import os
import shutil
import requests
from bs4 import BeautifulSoup

url = "https://wikiway.com/strani/" 

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }
req = requests.get(url, headers=headers) # получаем всю страницу
page = req.text # толучаем текст
# print(page)

soup = BeautifulSoup(page, "lxml")
all_country = soup.find_all(class_="country") # находим все страны
# print(all_country)

# пишем все в фаил
with open('backend/parsing/countries.html', "w") as file:
    file.write(str(all_country))

with open("backend/parsing/countries.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

all_country_href = soup.find_all('li')
all_country_dict ={}

for item in all_country_href:
    
    item_href = "https://wikiway.com" + item.find('a')['href']
    item_text = item.text[2:]
    # print(f"{item_text}: {item_href}")

    all_country_dict[item_text] = item_href

with open('backend/parsing/countries.json', "w") as file:
    json.dump(all_country_dict, file, indent=4, ensure_ascii=False)
    print("json country OK")

# Получаем одну страну
url = "https://wikiway.com/poland/"

req = requests.get(url, headers=headers) # получаем страницу со страной
page = req.text # толучаем текст
# print(page)

country = "poland"
# shutil.rmtree(f"backend/parsing/" + country) # удаляем папку
if os.path.exists(f"backend/parsing/" + country):    # Проверяем если папка существует.
    print(f"папка {country} есть")
else:
    os.mkdir(f"backend/parsing/" + country)

 

# пишем все в фаил
with open(f"backend/parsing/"+country+"/"+country+".html", "w") as file:
    file.write(str(page))

with open(f"backend/parsing/"+country+"/"+country+".html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
# название страны
country_name_dict = {}
country_name = soup.find('h1').get_text() # название страны
country_name_dict['country']=country_name
# print(country_name)

# описание страны
country_description_dict = {}
country_description = soup.find('p').get_text() # описание страны
country_description_dict['country_description']=country_description
# print(country_description)

# ссылки на фото страны
img = str(soup.find(class_="scroll").find(class_="scrolling-stone")) # ссылки на фото страны
soup = BeautifulSoup(img, "lxml")

img_src = soup.find_all('img')
img_url_dick = {}
i = 0
for src in img_src:
    img_url = "https://wikiway.com"+src['src']
    img_url_dick[f'img_url_{i}']=img_url
    i += 1
    # print(img_url)

# получаем все города
url = f"https://wikiway.com/{country}/goroda/" 
req = requests.get(url, headers=headers) # получаем всю страницу
page = req.text # толучаем текст
soup = BeautifulSoup(page, "lxml")
city = soup.find_all(class_="ob-tz")
city_name_dict = {}
c = 1
for city in city:
    city_name = city.text
    city_name_dict[f'city_name_{c}']=city_name
    c += 1
    
    # пишем в json
with open("backend/parsing/"+country+"/"+country+".json", "w") as file:
    json.dump([country_name_dict, country_description_dict, img_url_dick,city_name_dict], file, indent=4, ensure_ascii=False)
    
    print("json country OK")
