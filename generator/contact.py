from model.contact import Contact
from generator.generator_helpers import random_string, random_date
from datetime import date
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [Contact(firstname="Василий", mid_name="Иванович", lastname="Чапаев", nickname="chapa",
                    photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                    company_address="Новосибирск", home_tel="3303030", mobile_tel="89131112233",
                    work_tel="2872727", fax="111111", email="a.chapaev@mail.ru", email_2="a.chapaev@yandex.ru",
                    email_3="a.chapaev@gmail.ru", homepage="homepage.com", birthday=date(1887, 2, 7),
                    anniversary=date(1917, 3, 7), home_address="г. Новосибирск, ул. Ленина, 33",
                    home_tel_2="2870760", notes="Заметки123")] + [
    Contact(firstname=random_string("name", 10), mid_name=random_string("mid_name", 10),
            lastname=random_string("last_name", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 20), company_name=random_string("company_name", 15),
            company_address=random_string("company_address", 25), home_tel=random_string("home_tel", 10),
            mobile_tel=random_string("company_name", 10), work_tel=random_string("work_tel", 10),
            fax=random_string("fax", 10), email=random_string("email", 15), email_2=random_string("email_2", 15),
            email_3=random_string("email_3", 15), homepage=random_string("homepage", 15), birthday=random_date(),
            anniversary=random_date(), home_address=random_string("home_address", 20),
            home_tel_2=random_string("home_tel_2", 10), notes=random_string("notes", 40))
    for i in range(4)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w", encoding="utf-8") as out:
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False, indent=2)
    out.write(jsonpickle.encode(testdata))
