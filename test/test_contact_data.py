from helpers import create_contact_if_empty, merge_phones, merge_emails


def test_all_fields_on_home_page(app, orm):
    create_contact_if_empty(app, orm)
    contacts_from_homepage = app.contact.get_contacts_list()

    for c in contacts_from_homepage:
        contact_from_db = orm.get_contact_by_id(c.id)
        assert c.firstname == contact_from_db.firstname and c.lastname == contact_from_db.lastname
        assert c.company_address == contact_from_db.company_address
        assert c.all_emails_from_homepage == merge_emails(contact_from_db)
        assert c.all_phones_from_home_page == merge_phones(contact_from_db)


"""
def test_all_fields_on_home_page(app, orm):
    if len(orm.get_contact_list()) == 0:
        contact = Contact(firstname="Василий", mid_name="Иванович", lastname="Чапаев", nickname="chapa",
                          photo=os.path.abspath("../files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                          company_address="г. Новосибирск, ул. Мусы Джалиля, 11", home_tel="3303030",
                          mobile_tel="89131112233", work_tel="2872727", fax="111111", email="a.chapaev@mail.ru",
                          email_2="a.chapaev@yandex.ru", email_3="a.chapaev@gmail.ru", homepage="homepage.com",
                          birthday=date(1887, 2, 7), anniversary=date(1917, 3, 7),
                          home_address="г. Новосибирск, ул. Ленина, 33", home_tel_2="2870760", notes="Заметки123")
        app.contact.create(contact)
    contacts_from_homepage = app.contact.get_contacts_list()
    index = randrange(len(contacts_from_homepage))
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contacts_from_view_page(index)
    selected_contact = contacts_from_homepage[index]

    assert selected_contact.firstname == contact_from_edit_page.firstname and \
           selected_contact.lastname == contact_from_edit_page.lastname
    assert selected_contact.company_address == contact_from_edit_page.company_address
    assert selected_contact.all_emails_from_homepage == merge_emails(contact_from_edit_page)
    assert contacts_from_homepage[index].all_phones_from_home_page == merge_phones(contact_from_edit_page)
    assert merge_phones(contact_from_view_page) == merge_phones(contact_from_edit_page)
"""
