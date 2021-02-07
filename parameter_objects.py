

class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class Contact:

    def __init__(self, first_name, mid_name, last_name, nickname, photo, title, company_name, company_address,
                 home_tel, mobile_tel, work_tel, fax, email, email_2, email_3, homepage, birthday, anniversary,
                 home_address, home, notes):
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
        self.home = home
        self.notes = notes
