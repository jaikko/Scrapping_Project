import requests
from bs4 import BeautifulSoup

# Debut
url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
links_cat = []
links_books = []
list_cat = []
book_info = []


# Recuperer toutes les catégories
def get_categories():
    cats = soup.find(class_='nav nav-list')
    for i in cats:
        ul = cats.find('ul')
        li = ul.findAll('li')

    for i in li:
        a = i.find('a')
        link = a['href']
        categorie = a.text

        links_cat.append('http://books.toscrape.com/' + link)
        list_cat.append(categorie)


def get_all_book_by_categorie():
    num = 0
    max = 1

    for i in list_cat:
        url1 = links_cat[num]
        num += 1
        res = requests.get(url1)
        sp = BeautifulSoup(res.text, features="html.parser")
        page = sp.find(class_='current')
        result = sp.find(class_='form-horizontal')

        if result:
            nbre_str = result.text.replace(" ", "")
            nbre_result = nbre_str[3:5]

        if page:
            nbre_page = page.text.replace(" ", "")
            max_page = nbre_page[-3]
            max_page = max
            ints = int(nbre_result) / (int(max_page) * 20)

        books = sp.findAll(class_="image_container")
        count = 0
        for u in books:

            a = u.find('a')
            link = a['href']
            link_str = link.split("/")

            if not page:
                print("no enter")
                links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4])
                link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4]

            if page:
                print(count)
                print("page")

                if 140 > count <= 160:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-7.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-7.html"
                    count += 1
                if 120 > count <= 140:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-6.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-6.html"
                    count += 1
                if 100 > count <= 120:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-5.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-5.html"
                    count += 1
                if 100 > count <= 120:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-5.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-5.html"
                    count += 1
                if 100 > count <= 120:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-5.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-5.html"
                    count += 1
                if 80 > count <= 100:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-4.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-4.html"
                    count += 1
                    print(count)
                if 40 > count <= 60:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-3.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-3.html"
                    count += 1
                if count > 20:
                    print("ok")
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/page-2.html")
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + "/page-2.html"

                    count += 1
                if count <= 20:
                    links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4])
                    link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4]
                    count += 1
                    print("moins")


            get_book_info(link_final)


def get_book_info(url_book):
    res = requests.get(url_book)
    sp = BeautifulSoup(res.text, features="html.parser")

    # Ajouter titre à la liste
    title = sp.find('h1')
    book_info.append(title.text)


get_categories()
get_all_book_by_categorie()

[print(i) for i in book_info]
