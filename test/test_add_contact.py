# -*- coding: utf-8 -*-
from model.contact import Contact
from datetime import date
import os


def test_add_contact_all_fields(app):
    app.session.login(username="admin", password="secret")

    contact = Contact(first_name="Василий", mid_name="Иванович", last_name="Чапаев", nickname="chapa",
                      photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                      company_address="Новосибирск", home_tel="3303030", mobile_tel="89131112233",
                      work_tel="2872727", fax="111111", email="a.chapaev@mail.ru", email_2="a.chapaev@yandex.ru",
                      email_3="a.chapaev@gmail.ru", homepage="homepage.com", birthday=date(1887, 2, 7),
                      anniversary=date(1917, 3, 7), home_address="г. Новосибирск, ул. Ленина, 33",
                      home="qwertyasd", notes="Заметки123")

    app.contact.create(contact)
    app.session.logout()
