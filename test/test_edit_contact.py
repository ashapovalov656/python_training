from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(last_name="Новая_фамилия_2"))
