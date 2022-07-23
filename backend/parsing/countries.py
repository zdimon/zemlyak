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

city = "poland"
# shutil.rmtree(f"backend/parsing/" + city) # удаляем папку
if os.path.exists(f"backend/parsing/" + city):    # Проверяем если папка существует.
    print(f"папка {city} есть")
else:
    os.mkdir(f"backend/parsing/" + city)

 

# пишем все в фаил
with open(f"backend/parsing/"+city+"/"+city+".html", "w") as file:
    file.write(str(page))

with open(f"backend/parsing/"+city+"/"+city+".html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

city_name = soup.find('h1').get_text() # название города
# print(city_name)

city_description = soup.find('p').get_text() # описание города города
print(city_description)

