# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from parameter_objects import Contact
from datetime import date, datetime
import os

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def add_contact(self, wd, contact):
        # names
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.mid_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        # telephone numbers, photo, company, etc
        #wd.find_element_by_xpath("//input[@name='photo']").click()
        #wd.find_element_by_xpath("//input[@name='photo']").clear()
        wd.find_element_by_xpath("//input[@name='photo']").send_keys(contact.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_tel)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_tel)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_tel)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

        # emails
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        # birthday
        wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday.day)
        wd.find_element_by_xpath("//option[@value='" + str(contact.birthday.day) + "']").click()
        wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday.month)
        wd.find_element_by_xpath("//option[@value='"
                                 + datetime.strptime(str(contact.birthday.month), "%m").strftime("%B")
                                 + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday.year)

        # anniversary
        wd.find_element_by_name("aday").click()
        #Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary.day)
        wd.find_element_by_xpath("(//option[@value='" + str(contact.anniversary.day) + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary.month)
        wd.find_element_by_xpath("(//option[@value='"
                                 + datetime.strptime(str(contact.anniversary.month), "%m").strftime("%B")
                                 + "'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary.year)

        # home address, notes
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.home_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home").click()

# ===================== TESTS =====================

    def test_add_contact_all_fields(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")

        contact = Contact(first_name="Василий", mid_name="Иванович", last_name="Чапаев", nickname="chapa",
                          photo=os.path.abspath("files/chapaev.jpg"), title="my_title", company_name="ЦФТ",
                          company_address="Новосибирск", home_tel="3303030", mobile_tel="89131112233",
                          work_tel="2872727", fax="111111", email="a.chapaev@mail.ru", email_2="a.chapaev@yandex.ru",
                          email_3="a.chapaev@gmail.ru", homepage="homepage.com", birthday=date(1887, 2, 7),
                          anniversary=date(1917, 3, 7), home_address="г. Новосибирск, ул. Ленина, 33",
                          home="qwertyasd", notes="Заметки123")

        self.add_contact(wd, contact)
        self.return_to_homepage(wd)
        self.logout(wd)

# ===================== /TESTS =====================

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
