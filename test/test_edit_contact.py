from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Default_name", last_name="Default_lastname"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Новое_имя", last_name="Новая_фамилия_2")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

