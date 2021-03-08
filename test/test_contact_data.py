from model.contact import Contact
from datetime import date
import os
from random import randrange


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email_2, contact.email_3])))


def test_all_fields_on_home_page(app):
    if app.contact.count() == 0:
        contact = Contact(first_name="Василий", mid_name="Иванович", last_name="Чапаев", nickname="chapa",
                          photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                          company_address="г. Новосибирск, ул. Мусы Джалиля, 11", home_tel="3303030",
                          mobile_tel="89131112233", work_tel="2872727", fax="111111", email="a.chapaev@mail.ru",
                          email_2="a.chapaev@yandex.ru", email_3="a.chapaev@gmail.ru", homepage="homepage.com",
                          birthday=date(1887, 2, 7), anniversary=date(1917, 3, 7),
                          home_address="г. Новосибирск, ул. Ленина, 33", home_tel_2="2870760", notes="Заметки123")
        app.contact.create(contact)
    all_contacts = app.contact.get_contacts_list()
    index = randrange(len(all_contacts))
    selected_contact = all_contacts[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)

    assert selected_contact.first_name == contact_from_edit_page.first_name and \
           selected_contact.last_name == contact_from_edit_page.last_name

    assert selected_contact.company_address == contact_from_edit_page.company_address

    assert selected_contact.all_emails_from_homepage == merge_emails(contact_from_edit_page)
