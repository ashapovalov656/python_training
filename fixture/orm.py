from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        company_address = Optional(str, column="address")
        email = Optional(str, column="email")
        email_2 = Optional(str, column="email2")
        email_3 = Optional(str, column="email3")
        home_tel = Optional(str, column="home")
        mobile_tel = Optional(str, column="mobile")
        work_tel = Optional(str, column="work")
        home_tel_2 = Optional(str, column="phone2")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, db_name, user, password):
        self.db.bind('mysql', host=host, database=db_name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(c):
            return Contact(id=str(c.id), firstname=c.firstname, lastname=c.lastname, company_address=c.company_address,
                           email=c.email, email_2=c.email_2, email_3=c.email_3, home_tel=c.home_tel,
                           mobile_tel=c.mobile_tel, work_tel=c.work_tel, home_tel_2=c.home_tel_2)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contact_by_id(self, id):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None
                                                     and str(c.id) == id))[0]
