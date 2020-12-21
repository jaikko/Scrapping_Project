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

book_info = []
book1 = Book('test', '1fghj', 'test', '15', '15', '2', '', 'libre', '2/5', 'url')
book_info.append(book1)







def extract_to_csv(output_file, delimiter="\t"):
    with open(output_file, "w", encoding='utf-8') as output_file:
        # for i in header:
        # output_file.write(i + '\t')

        cc = 0
        header = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                  "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                  "image_url"]
        for head in header:
            output_file.write(head + "*" + '\t')

        output_file.write('\n')

        for li in book_info:
            book = li.val()
            for info in book:
                print(info)
                output_file.write(info + "*" + '\t')
                cc += 1
                if cc == 10:
                    output_file.write('\n')
                    cc = 0


extract_to_csv("test.csv")