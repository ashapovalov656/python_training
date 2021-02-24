from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Default_name"))
    app.contact.edit_first_contact(Contact(last_name="Новая_фамилия_2"))
