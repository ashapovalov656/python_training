from datetime import datetime
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.mid_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)

        if contact.photo:
            wd.find_element_by_xpath("//input[@name='photo']").send_keys(contact.photo)

        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.company_address)
        self.change_field_value("home", contact.home_tel)
        self.change_field_value("mobile", contact.mobile_tel)
        self.change_field_value("work", contact.work_tel)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)

        if contact.birthday:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(str(contact.birthday.day))
            wd.find_element_by_name("bmonth").click()
            wd.find_element_by_xpath("//option[@value='"
                                     + datetime.strptime(str(contact.birthday.month), "%m").strftime("%B")
                                     + "']").click()
            self.change_field_value("byear", contact.birthday.year)

        if contact.anniversary:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary.day))
            wd.find_element_by_name("amonth").click()
            wd.find_element_by_xpath("(//option[@value='"
                                     + datetime.strptime(str(contact.anniversary.month), "%m").strftime("%B")
                                     + "'])[2]").click()
            self.change_field_value("ayear", contact.anniversary.year)

        self.change_field_value("address2", contact.home_address)
        self.change_field_value("phone2", contact.home)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_homepage()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))



