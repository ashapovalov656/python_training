from model.contact import Contact
import random


def test_delete_contact_by_id(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Default_name", lastname="Default_lastname"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == len(orm.get_contact_list())
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
