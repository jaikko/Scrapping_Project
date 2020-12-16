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
links_other_page = []
links_all_page = []


# Recuperer toutes les catégories
def get_categories():
    cats = soup.find(class_='nav nav-list')

    ul = cats.find('ul')
    li = ul.findAll('li')

    for i in li:
        a = i.find('a')
        link = a['href']

        categorie = a.text.replace(" ", "").strip('\n')
        links_cat.append('http://books.toscrape.com/' + link)
        list_cat.append(categorie)


def get_number_page():
    num = 0
    ind = 1

    for i in list_cat:
        url1 = links_cat[num]

        num += 1
        ind += 1
        res = requests.get(url1)
        sp = BeautifulSoup(res.text, features="html.parser")
        page = sp.find(class_='current')
        if page:
            nbre_page = page.text.replace(" ", "")
            max_page = nbre_page[-3]
            for j in range(int(max_page)-1):
                url2 = 'http://books.toscrape.com/catalogue/category/books/' + i.replace(" ", "").lower().strip('\n') + "_" + str(ind) + "/page-" + str(j + 2) + ".html"
                links_other_page.append(url2)


def get_all_book_by_categorie():
    num = 0
    max = 1

    for i in list_cat:
        links_all_page.clear()
        url1 = links_cat[num]
        links_all_page.append(url1)

        matching = filter(lambda x: i.lower() in x, links_other_page)

        for k in matching:
            links_all_page.append(k)

        num += 1

        for link in links_all_page:
            res = requests.get(link)
            sp = BeautifulSoup(res.text, features="html.parser")
            page = sp.find(class_='current')
            result = sp.find(class_='form-horizontal')

            books = sp.findAll(class_="image_container")

            #Création url du livre
            for u in books:
                a = u.find('a')
                link = a['href']
                link_str = link.split("/")

                links_books.append('http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4])
                link_final = 'http://books.toscrape.com/catalogue/' + link_str[3] + "/" + link_str[4]

                get_book_info(link_final)


        extract_to_csv(book_info,i+".csv")



def extract_to_csv(liste, output_file, delimiter="\t"):
    header = ["universal_ product_code (upc)","title","price_including_tax", "price_excluding_tax",
              "number_available","product_description","category","review_rating", "image_url"]
    with open(output_file, "w") as output_file:

        for i in header:

            output_file.write(i + '\t')

        output_file.write('\n')
        for i in liste:

            output_file.write(str(i) + '\t')

def get_book_info(url_book):
    res = requests.get(url_book)
    sp = BeautifulSoup(res.text, features="html.parser")

    # Ajouter titre à la liste
    title = sp.find('h1')
    book_info.append(title.text)


get_categories()
get_number_page()
get_all_book_by_categorie()


