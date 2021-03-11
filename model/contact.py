from sys import maxsize


class Contact:

    def __init__(self, id=None, first_name=None, mid_name=None, last_name=None, nickname=None, photo=None, title=None,
                 company_name=None, company_address=None, home_tel=None, mobile_tel=None, work_tel=None, fax=None,
                 email=None, email_2=None, email_3=None, homepage=None, birthday=None, anniversary=None,
                 home_address=None, home_tel_2=None, notes=None, all_phones_from_home_page=None,
                 all_emails_from_homepage=None):
        self.id = id
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company_name = company_name
        self.company_address = company_address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday = birthday
        self.anniversary = anniversary
        self.home_address = home_address
        self.home_tel_2 = home_tel_2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "id=%s\n" \
               "first_name=%s\n" \
               "mid_name=%s\n" \
               "last_name=%s\n" \
               "nickname=%s\n" \
               "title=%s\n" \
               "company_name=%s\n" \
               "company_address=%s\n" \
               "home_tel=%s\n" \
               "mobile_tel=%s\n" \
               "work_tel=%s\n" \
               "fax=%s\n" \
               "email=%s\n" \
               "email_2=%s\n" \
               "email_3=%s\n" \
               "homepage=%s\n" \
               "birthday=%s\n" \
               "anniversary=%s\n" \
               "home_address=%s\n" \
               "home_tel_2=%s\n" \
               "notes=%s" % (self.id, self.first_name, self.mid_name, self.last_name, self.nickname, self.title,
                             self.company_name, self.company_address, self.home_tel, self.mobile_tel, self.work_tel,
                             self.fax, self.email, self.email_2, self.email_3, self.homepage, self.birthday,
                             self.anniversary, self.home_address, self.home_tel_2, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.first_name == other.first_name) \
               and (self.last_name == other.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
