from faker import Faker
import timeit

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'

class BusinessContact (BaseContact):
    def __init__(self, position, company, workphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.workphone = workphone
    
    def __str__(self):
        return super().__str__() + f' {self.position} {self.company} {self.workphone}'

def measure_time (func):
    def timer():
        start_time = timeit.default_timer()
        result = func()
        end_time = timeit.default_timer()
        print (end_time-start_time)
        return result
    return timer 

@measure_time

def create_contacts ():
    fake = Faker()
    new_friends = []
    for _ in range(1000):
        new_card = None
        new_card = BaseContact (fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_company_email())
        new_friends.append (new_card)
    return new_friends

create_contacts()     


