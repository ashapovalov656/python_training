from model.contact import Contact
from model.group import Group
from datetime import date
import os
import re


def create_contact_if_empty(app, orm):
    if len(orm.get_contact_list()) == 0:
        contact = Contact(firstname="Василий", mid_name="Иванович", lastname="Чапаев", nickname="chapa",
                          photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                          company_address="г. Новосибирск, ул. Мусы Джалиля, 11", home_tel="3303030",
                          mobile_tel="89131112233", work_tel="2872727", fax="111111", email="a.chapaev@mail.ru",
                          email_2="a.chapaev@yandex.ru", email_3="a.chapaev@gmail.ru", homepage="homepage.com",
                          birthday=date(1887, 2, 7), anniversary=date(1917, 3, 7),
                          home_address="г. Новосибирск, ул. Ленина, 33", home_tel_2="2870760", notes="Заметки123")
        app.contact.create(contact)


def clear(s):
    return re.sub("[() -]", "", s).\
        replace(".", "").\
        replace("/", "")


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel, contact.work_tel, contact.home_tel_2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: " ".join(x.split()),
                                filter(lambda x: x is not None, [contact.email, contact.email_2, contact.email_3]))))


def create_group_if_empty(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="default group", header="default header", footer="default footer"))
