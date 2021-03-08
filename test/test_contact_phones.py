import re
from random import randrange
from model.contact import Contact


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel, contact.work_tel, contact.home_tel_2]))))


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Default_name", last_name="Default_lastname", home_tel="838312345",
                                   home_tel_2="3306871", mobile_tel="+7-913-123-45-67", work_tel="+7(383)2219876"))
    contacts_from_homepage = app.contact.get_contacts_list()
    index = randrange(len(contacts_from_homepage))
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contacts_from_homepage[index].all_phones_from_home_page == merge_phones(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Default_name", last_name="Default_lastname", home_tel="838312345",
                                   home_tel_2="3306871", mobile_tel="+7-913-123-45-67", work_tel="+7(383)2219876"))
    contacts_from_homepage = app.contact.get_contacts_list()
    index = randrange(len(contacts_from_homepage))
    contact_from_view_page = app.contact.get_contacts_from_view_page(index)
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert merge_phones(contact_from_view_page) == merge_phones(contact_from_edit_page)
