import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")


def find_all_table():
    if response.ok:
        tables = soup.find_all("table")
        return tables


listes = []


def table_to_csv(table, output_file, delimiter="\t"):
    td_set = table.find_all("td")
    th_set = table.find_all("th")

    for z in range(len(td_set)-1):
        for i in range(len(th_set)-1):
            th_data = th_set[i].text.rstrip('\n')
            if th_data == "UPC":
                td_data = td_set[z].text.rstrip('\n')




all_tables = find_all_table()
table_to_extract = all_tables[0]

table_to_csv(table_to_extract, "test.csv")
title = soup.find('h1')
product_page_url = ""



stock = soup.find(class_="instock availability")

all_th = soup.findAll('td')

for i in all_th:
    th_data = i.text.rstrip('\n')
    listes.append(th_data)

del listes[1]
del listes[3:6]

dict_book= {}

def generate_dict():
    info_dict=["universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
    "number_available", "product_description", "category", "review_rating", "image_url"]
    for i in info_dict:
        dict_book[i] = "robert"

generate_dict()

for cle, value in dict_book.items():
     print (cle, value)
