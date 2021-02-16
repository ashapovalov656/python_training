

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_lastname("Новая_фамилия")
    app.session.logout()
