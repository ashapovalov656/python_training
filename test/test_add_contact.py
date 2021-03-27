# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts, orm, check_ui):
    contact = json_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == len(orm.get_contact_list())
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
