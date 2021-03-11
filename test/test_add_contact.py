# -*- coding: utf-8 -*-
from model.contact import Contact
from datetime import date
import os
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="Василий", mid_name="Иванович", last_name="Чапаев", nickname="chapa",
                    photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                    company_address="Новосибирск", home_tel="3303030", mobile_tel="89131112233",
                    work_tel="2872727", fax="111111", email="a.chapaev@mail.ru", email_2="a.chapaev@yandex.ru",
                    email_3="a.chapaev@gmail.ru", homepage="homepage.com", birthday=date(1887, 2, 7),
                    anniversary=date(1917, 3, 7), home_address="г. Новосибирск, ул. Ленина, 33",
                    home_tel_2="2870760", notes="Заметки123")] + [
    Contact(first_name=random_string("name", 10), mid_name=random_string("mid_name", 10),
            last_name=random_string("last_name", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 20), company_name=random_string("company_name", 15),
            company_address=random_string("company_address", 25), home_tel=random_string("home_tel", 10),
            mobile_tel=random_string("company_name", 10), work_tel=random_string("work_tel", 10),
            fax=random_string("fax", 10), email=random_string("email", 15), email_2=random_string("email_2", 15),
            email_3=random_string("email_3", 15), homepage=random_string("homepage", 15),
            birthday=date(random.randrange(3000), random.randrange(1, 13), random.randrange(1, 32)),
            anniversary=date(random.randrange(3000), random.randrange(1, 13), random.randrange(1, 32)),
            home_address=random_string("home_address", 20), home_tel_2=random_string("home_tel_2", 10),
            notes=random_string("notes", 40))
    for i in range(4)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
