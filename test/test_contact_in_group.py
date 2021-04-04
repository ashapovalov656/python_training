from helpers import create_contact_if_empty, create_group_if_empty
from model.contact import Contact
import random


def test_add_contact_to_group(app, orm, check_ui):
    create_contact_if_empty(app, orm)
    create_group_if_empty(app, orm)
    groups = orm.get_group_list()

    contact = None
    group = None
    for g in groups:
        contacts_not_in_group = orm.get_contacts_not_in_group(g)
        if len(contacts_not_in_group) != 0:
            contact = random.choice(contacts_not_in_group)
            group = g
            break

    if contact is None:
        app.contact.create(Contact(firstname="Имя", mid_name="Отчество", lastname="Фамилия"))
        group = random.choice(groups)
        contact = orm.get_contacts_not_in_group(group)[0]

    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)

    if check_ui:
        assert app.contact.check_contact_in_group(group.id, contact.id)


def test_delete_contact_from_group(app, orm, check_ui):
    create_contact_if_empty(app, orm)
    create_group_if_empty(app, orm)

    groups = orm.get_group_list()
    contact = None
    group = None
    for g in groups:
        contacts_in_group = orm.get_contacts_in_group(g)
        if len(contacts_in_group) != 0:
            contact = random.choice(contacts_in_group)
            group = g
            break

    if contact is None:
        contact = random.choice(orm.get_contact_list())
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id)

    app.contact.del_contact_from_group(group.id, contact.id)
    assert contact not in orm.get_contacts_in_group(group)

    if check_ui:
        assert not app.contact.check_contact_in_group(group.id, contact.id)
