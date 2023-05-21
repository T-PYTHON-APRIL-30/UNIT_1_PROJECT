import requests
from bs4 import BeautifulSoup as bs   
import re 
import csv
import selen



# url = "https://www.extra.com/en-sa/computer/c/3/facet/brandEn:HUAWEI:familyEn:Computers%20Accessories:familyEn:Laptops:familyEn:Monitors?q=:relevance:brandEn:HUAWEI:familyEn:Computers%20Accessories:familyEn:Laptops:familyEn:Monitors:inStock:true&text=&pageSize=24&pg=0&sort=price-desc"
# page = requests.get(url  )

# def main(page:requests.Response):
#     src = page.content
#     soup = bs(src, "lxml")
#     print(soup)
#     # print(soup.text)
#     matches = []
#     card_items = soup.find_all(name='div', attrs={"class": "page"})
#     print(card_items)

# main(page)

# # with open("my.html", "+a", encoding="utf-8") as file :
# #     file.write(r.text)

# soup = bs(r.content, "html5lib")
# table = soup.find('div', attrs={'class': "product-tile__item"})
# print(table.prettify())

