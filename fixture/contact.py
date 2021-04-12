from datetime import datetime
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    contact_cache = None

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

        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.mid_name)
        self.change_field_value("lastname", contact.lastname)
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
        self.change_field_value("phone2", contact.home_tel_2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_homepage()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_homepage()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_homepage()
        self.contact_cache = None

    def edit_contact_by_id(self, contact):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % contact.id).click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_homepage()
        self.contact_cache = None

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()
        wd.find_element_by_name("add").click()
        self.app.open_homepage()
        self.contact_cache = None

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % contact_id).click()

    def count(self):
        wd = self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                company_address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=first_name, lastname=last_name,
                                                  all_phones_from_home_page=all_phones,
                                                  company_address=company_address, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        mobile_tel = wd.find_element_by_name("mobile").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        home_tel_2 = wd.find_element_by_name("phone2").get_attribute("value")
        company_address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_tel=home_tel,
                       mobile_tel=mobile_tel, work_tel=work_tel, home_tel_2=home_tel_2, company_address=company_address,
                       email=email, email_2=email_2, email_3=email_3)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
        home_tel_2 = re.search("P: (.*)", text).group(1)
        return Contact(home_tel=home_tel, mobile_tel=mobile_tel, work_tel=work_tel, home_tel_2=home_tel_2)

    def open_contacts_in_group(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()

    def check_contact_in_group(self, group_id, contact_id):
        wd = self.app.wd
        self.app.open_homepage()
        self.open_contacts_in_group(group_id)

        if len(wd.find_elements_by_css_selector("input[id='%s']" % contact_id)) == 1:
            return True

        return False

    def del_contact_from_group(self, group_id, contact_id):
        wd = self.app.wd
        self.app.open_homepage()
        self.open_contacts_in_group(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
