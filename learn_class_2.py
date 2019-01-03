##employee profile with first name, last, pay, email
##
##generate an email address form the first and last name and @company.com suffix
##generate the full name as a method


class Employee:

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first.lower()+'.'+last.lower()+'@company.com'

    def fullname(self):
        return self.first+' '+self.last

emp_1=Employee('Pat', 'Nicoles', 40000)
emp_2=Employee('Daisy','Sandrea',42000)

print(emp_2.email)
print(emp_1.fullname())
