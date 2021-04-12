from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given("a contact list", target_fixture="contact_list")
def contact_list(orm):
    return orm.get_contact_list()


@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Default name", mid_name="Default mid name", lastname="Default lastname"))
    return orm.get_contact_list()


@given("a contact with <firstname>, <mid_name> and <lastname>", target_fixture="new_contact")
def new_contact(firstname, mid_name, lastname):
    return Contact(firstname=firstname, mid_name=mid_name, lastname=lastname)


@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@given("a modified random contact with the new <firstname> and <lastname>", target_fixture="modified_contact")
def modified_contact(random_contact, firstname, lastname):
    random_contact.firstname = firstname
    random_contact.lastname = lastname
    return random_contact


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@when("I modify the contact")
def modify_contact(app, modified_contact):
    app.contact.edit_contact_by_id(modified_contact)


@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(orm, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(orm, non_empty_contact_list, random_contact, check_ui, app):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == len(orm.get_contact_list())
    new_contacts = orm.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@then("the new contact list is equal to the old list with the modified contact")
def verify_contact_modified(orm, non_empty_contact_list, modified_contact, check_ui, app):
    old_contacts = non_empty_contact_list
    new_contacts = orm.get_contact_list()

    for c in old_contacts:
        if c.id == modified_contact.id:
            idx = old_contacts.index(c)
            old_contacts[idx] = modified_contact
            break

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
