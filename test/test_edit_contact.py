from model.contact import Contact
from helpers import create_contact_if_empty
from random import randrange


def test_edit_contact_by_id(app, orm, check_ui):
    create_contact_if_empty(app, orm)
    old_contacts = orm.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(id=old_contacts[index].id, firstname="Новое_имя", lastname="Новая_фамилия")
    app.contact.edit_contact_by_id(contact, contact.id)
    assert len(old_contacts) == len(orm.get_contact_list())
    new_contacts = orm.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
