

class Book:
    list = []
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def aff(self):
        print(self.nom)
    def val(self):
        return [self.nom, str(self.prix)]



list_obj = [

]
book1 = Book("jkjkj", 15)
book2 = Book("jkhjhkj", 15)
list_obj.append(book1)
list_obj.append(book2)


for j in list_obj:
    j.aff()

with open("output_file.csv", "w", encoding='utf-8') as output_file:
    # for i in header:
    # output_file.write(i + '\t')

    for li in list_obj:
        po = li.val()


        cc = 0
        for i in po:
            cc += 1
            output_file.write(i + '\t')
            if cc == 2:
                output_file.write('\n')
                cc = 0


