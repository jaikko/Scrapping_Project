import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")


def find_all_table():
    if response.ok:
        tables = soup.find_all("table")
        return tables


def table_to_csv(table, output_file, delimiter="\t"):
    with open(output_file, "w") as output_file:
        header = ""
        th_set = table.find_all("th")
        for i in range(len(th_set)):
            th_data = th_set[i].text.rstrip('\n')
            if i == len(th_set) - 1:
                header += f"{th_data}\n"
            else:
                header += f"{th_data}{delimiter}"
        output_file.write(header)

all_tables = find_all_table()
table_to_extract = all_tables[0]


table_to_csv(table_to_extract,  "test.csv")
title = soup.find('h1')
product_page_url = ""

stock = soup.find(class_="instock availability")
print(title.text)
print(stock.text)
