from datetime import datetime
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd

        if contact.first_name:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.first_name)

        if contact.mid_name:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.mid_name)

        if contact.last_name:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.last_name)

        if contact.nickname:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)

        if contact.photo:
            wd.find_element_by_xpath("//input[@name='photo']").send_keys(contact.photo)

        if contact.title:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)

        if contact.company_name:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company_name)

        if contact.company_address:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.company_address)

        if contact.home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_tel)

        if contact.mobile_tel:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_tel)

        if contact.work_tel:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_tel)

        if contact.fax:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.fax)

        if contact.email:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)

        if contact.email_2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email_2)

        if contact.email_3:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email_3)

        if contact.homepage:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)

        if contact.birthday:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(str(contact.birthday.day))
            wd.find_element_by_name("bmonth").click()
            wd.find_element_by_xpath("//option[@value='"
                                     + datetime.strptime(str(contact.birthday.month), "%m").strftime("%B")
                                     + "']").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.birthday.year)

        if contact.anniversary:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary.day))
            wd.find_element_by_name("amonth").click()
            wd.find_element_by_xpath("(//option[@value='"
                                     + datetime.strptime(str(contact.anniversary.month), "%m").strftime("%B")
                                     + "'])[2]").click()
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.anniversary.year)

        if contact.home_address:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.home_address)

        if contact.home:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.home)

        if contact.notes:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.notes)

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



