from selenium.webdriver.firefox.webdriver import WebDriver
from datetime import datetime
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def add_contact(self, contact):
        wd = self.wd
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
        # wd.find_element_by_xpath("//input[@name='photo']").click()
        # wd.find_element_by_xpath("//input[@name='photo']").clear()
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
        Select(wd.find_element_by_name("bday")).select_by_visible_text(str(contact.birthday.day))
        wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday.month)
        wd.find_element_by_xpath("//option[@value='"
                                 + datetime.strptime(str(contact.birthday.month), "%m").strftime("%B")
                                 + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday.year)

        # anniversary
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary.day))
        wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary.month)
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
        self.return_to_homepage()

    def destroy(self):
        self.wd.quit()
