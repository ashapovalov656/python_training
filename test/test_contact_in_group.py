from model.contact import Contact
from helpers import create_contact_if_empty, create_group_if_empty
import random


def test_add_contact_to_group(app, orm, check_ui):
    create_contact_if_empty(app, orm)
    create_group_if_empty(app, orm)
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)

    if check_ui:
        assert app.contact.check_contact_in_group(group.id, contact.id)


def test_delete_contact_from_group(app, orm, check_ui):
    create_contact_if_empty(app, orm)
    create_group_if_empty(app, orm)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)

    if len(contact.groups) == 0:
        groups = orm.get_group_list()
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id)
        contact.groups.append(group)

    group = random.choice(contact.groups)
    app.contact.del_contact_from_group(group.id, contact.id)
    assert contact not in orm.get_contacts_in_group(group)

    if check_ui:
        assert not app.contact.check_contact_in_group(group.id, contact.id)
