import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group
import re


"""
db = DbFixture(host="127.0.0.1", db_name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))

    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))

finally:
    db.destroy()
"""

db = ORMFixture(host="127.0.0.1", db_name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))

    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))

    l = db.get_contacts_in_group(Group(id="294"))
    for contact in l:
        print(contact)
    print(len(l))

    l1 = db.get_contacts_not_in_group(Group(id="294"))
    for contact in l1:
        print(contact)
    print(len(l1))

finally:
    pass
    #db.destroy()
