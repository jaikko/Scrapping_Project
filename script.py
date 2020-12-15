import requests
from bs4 import BeautifulSoup

#Récupérer url
def get_url():
    all = soup.findAll(class_="image_container")
    for i in all:
        a = all.find('a')
        link = a['href']
        links.append('http://books.toscrape.com' + link)


#Variable
liste = []
links = []
url = 'http://books.toscrape.com/'



response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")










#Trouver le tableau dans le HTML
def find_all_table():
    if response.ok:
        tables = soup.find_all("table")
        return tables

#Récuperer les données du tableau
def get_table_data(table):
    th_set = table.find_all("th")
    td_set = table.find_all("td")
    for i in range(len(td_set)):
        if th_set[i].text == 'UPC':
            data = td_set[i].text.rstrip('\n')
            liste.append(data)
        elif th_set[i].text == 'Price (excl. tax)':
            data = td_set[i].text.rstrip('\n')
            liste.append(data)
        elif th_set[i].text == 'Price (incl. tax)':
            data = td_set[i].text.rstrip('\n')
            liste.append(data)
        elif th_set[i].text == 'Availability':
            data = td_set[i].text.rstrip('\n')
            liste.append(data)

#Ajouter info à la liste
def add(elem):
    liste.append(elem)

#Ajouter note à la liste
def add_review():
    note = soup.find_all('p')
    note_str = note[2].get_attribute_list('class')
    note_end = note_str[1]

    if note_end == "One":
        review = "1/5"
    elif note_end == "Two":
        review = "2/5"
    elif note_end == "Three":
        review = "3/5"
    elif note_end == "Four":
        review = "4/5"
    elif note_end == "Five":
        review = "5/5"

    add(review)

#Récupérer url
def get_url():
    ll = soup.findAll(class_="image_container")
    for i in ll:
        a = i.find('a')
        link = a['href']
        links.append('http://books.toscrape.com' + link)

        [print(i) for i in links]







#Ajouter titre à la liste
title = soup.find('h1')
add(title.text)

#Ajouter description à la lsite
desc = soup.find_all('p')
desc_livre= desc[3]
add(desc_livre.text)


#Ajouter Image URL
images = soup.findAll('img')
for image in images:
    img_url = image['src']
add(img_url)

#Ajouter catégorie
cat = soup.find_all('a', href=True)
cat_str = cat[3]
add(cat_str)

get_url()

add_review()

all_tables = find_all_table()

table_to_extract = all_tables[0]


get_table_data(table_to_extract)



def table_to_csv(liste, output_file, delimiter="\t"):
    header = ["universal_ product_code (upc)","title","price_including_tax", "price_excluding_tax",
              "number_available","product_description","category","review_rating", "image_url" ]
    with open(output_file, "w") as output_file:

        for i in header:

            output_file.write(i + '\t')

        output_file.write('\n')
        for i in liste:

            output_file.write(str(i) + '\t')

table_to_csv(liste, "test.csv")