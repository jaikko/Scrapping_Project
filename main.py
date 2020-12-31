import os
import urllib

import requests
from bs4 import BeautifulSoup

# Creation des dossiers
if not os.path.isdir("./CSV"):
    os.mkdir("./CSV")

if not os.path.isdir("./Images"):
    os.mkdir("./Images")

# Debut
url = 'http://books.toscrape.com/'
response = requests.get(url)
if response:
    soup = BeautifulSoup(response.text, features="html.parser")

# Liste
links_cat = []
links_books = []
list_cat = []
book_info = []
links_all_page = []


# classe Book
class Book:
    def __init__(self, product_page_url, upc, title, price_incl, price_excl, number_available, product_description,
                 category, review_rating, image_url):
        self.title = title
        self.price_incl = price_incl
        self.price_excl = price_excl
        self.upc = upc
        self.product_page_url = product_page_url
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.review_rating = review_rating
        self.image_url = image_url

    def val(self):
        return [self.product_page_url, self.upc, self.title, str(self.price_incl), str(self.price_excl),
                str(self.number_available), self.product_description, self.category, self.review_rating, self.image_url]

    def return_url_title(self):
        return [self.title, self.image_url]


# Recuperer toutes les catégories
def get_categories():
    cats = soup.find(class_='nav nav-list')

    ul = cats.find('ul')
    li = ul.findAll('li')

    for i in li:
        a = i.find('a')
        link = a['href']

        categorie = a.text.replace(" ", "").strip('\n')
        links_cat.append(url + link)
        list_cat.append(categorie)


def get_number_page(url_cat):
    max_page = ""
    res = requests.get(url_cat)
    sp = BeautifulSoup(res.text, features="html.parser")
    page = sp.find(class_='current')
    if page:
        nbre_page = page.text.replace(" ", "")
        max_page = nbre_page[-3]

    return max_page


def get_all_book_by_categorie():
    num = 0
    ind = 2

    for i in list_cat:
        links_all_page.clear()
        book_info.clear()
        url1 = links_cat[num]
        links_all_page.append(url1)
        
        categorie = url1.split('/')[-2]
        if ind >= 10:
            categorie = categorie[:-3]
        else:
            categorie = categorie[:-2]


        max_page = get_number_page(url1)
       
        if max_page != "":

            for j in range(int(max_page) - 1):
                url2 = url + 'catalogue/category/books/' + categorie.lower() + "_" + str(ind) \
                       + "/page-" + str(j + 2) + ".html"

                links_all_page.append(url2)

        for link in links_all_page:
            res = requests.get(link)
            sp = BeautifulSoup(res.text, features="html.parser")
            books = sp.findAll(class_="image_container")

            # Création url du livre
            for u in books:
                a = u.find('a')
                link = a['href']
                link_str = link.split("/")

                links_books.append(url + 'catalogue/' + link_str[3] + "/" + link_str[4])
                link_final = url + 'catalogue/' + link_str[3] + "/" + link_str[4]

                get_book_info(link_final, i)

        # Téléchargement Image
        download_save_image()
        # Extraction vers csv
        extract_to_csv(i + ".csv")

        ind += 1
        num += 1


def extract_to_csv(output_file):
    with open("./CSV/" + output_file, "w", encoding='utf-8') as output_file:

        cc = 0
        header = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                  "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                  "image_url"]
        for head in header:
            output_file.write(head + "|" + '\t')

        output_file.write('\n')

        for li in book_info:
            book = li.val()
            for info in book:

                output_file.write(info + "|" + '\t')
                cc += 1
                if cc == 10:
                    output_file.write('\n')
                    cc = 0


def get_book_info(url_book, cat):

    res = requests.get(url_book)
    sp = BeautifulSoup(res.content, features="html.parser")

    table = read_table(sp)
    # Traiter information du tableau
    upc = table[0]
    p_inc = table[1]
    p_inc = p_inc[1:].replace("Â", "")
    p_excl = table[2]
    p_excl = p_excl[1:]
    stock = table[3]

    # Récuper le stock
    stock = stock.split(" ")
    if not stock:
        stock = ""
    else:
        stock = stock[2].replace("(", "")

    # Ajouter description
    description = sp.find("div", {"id": "product_description"})
    if description:
        desc = sp.find_all('p')[3]
        desc = desc.text
    else:
        desc = ""

    # Ajouter titre
    title = sp.find('h1')
    if not title:
        title = ""
    else:
        title = title.text

    # Ajouter note

    note = sp.find_all('p')
    note = note[2].get_attribute_list('class')

    if not note:
        note = ""
    else:
        note = note[1]
    review = ""

    if note == "One":
        review = "1/5"
    elif note == "Two":
        review = "2/5"
    elif note == "Three":
        review = "3/5"
    elif note == "Four":
        review = "4/5"
    elif note == "Five":
        review = "5/5"

    # Ajouter Image URL

    image = sp.find(class_='item active')
    image = image.find('img')

    if not image:

        img = ""
    else:

        img = image['src']
        img = url + img[6:]

    # Création objet Book
    book = Book(url_book, upc, title, p_inc, p_excl, stock, desc, cat, review, img)

    # Ajouter objet Book à une liste
    book_info.append(book)


def read_table(sp):
    list_th = []
    list_th.clear()
    all_th = sp.findAll('td')

    for i in all_th:
        th_data = i.text.rstrip('\n')
        list_th.append(th_data)

    # retirer informations inutiles
    del list_th[1]
    del list_th[3:4]
    del list_th[-1]

    # retourner liste avec UPC, les deux prix et stock
    return list_th


def download_save_image():
    for li in book_info:
        book = li.return_url_title()
        ext = book[1].split('/')[-1].split(".")
        ext = ext[1]
        url_img = book[1]
        name = str(book[0])
        list_error = [":", "/", "\\", "*", "|", "?", '"', "<", ">"]
        for error in list_error:
            if error in name:
                name = name.replace(error, "")

        urllib.request.urlretrieve(url_img, "Images/" + name + "." + ext)


if response:
    get_categories()

    get_all_book_by_categorie()
else:
    print('site introuvable')
