from faker import Faker

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'

    def contact (self):
        return ("Wybieram %s %s i dzwonię do %s" % (self.name, self.surname, self.phone))
    @property
    def label_length (self):
        return (len(self.name) + 1 + len(self.surname))  

class BusinessContact (BaseContact):
    def __init__(self, position, company, workphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.workphone = workphone
    
    def __str__(self):
        return super().__str__() + f' {self.position} {self.company} {self.workphone}'

    def contact (self):
        return ("Wybieram %s %s i dzwonię do %s" % (self.name, self.surname, self.workphone))

def create_contacts (type_of_card, number):
    fake = Faker()
    new_friends = []
    for _ in range(number):
        new_card = None
        if type_of_card == "BaseContact":
            new_card = BaseContact (fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_company_email())
        elif type_of_card == "BusinessContact":
            new_card = BusinessContact (fake.job(), fake.company(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_company_email())
        new_friends.append (new_card)
    return new_friends 

test_contacts = create_contacts("BaseContact", 10)

by_name = sorted(test_contacts, key=lambda friend: friend.name)
by_surname = sorted(test_contacts, key=lambda friend: friend.surname)
by_email = sorted(test_contacts, key=lambda friend: friend.email)
