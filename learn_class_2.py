##employee profile with first name, last, pay, email
##
##generate an email address form the first and last name and @company.com suffix
##generate the full name as a method


class Employee:

    ##class variable
    pay_raise = 1


    def __init__(self, first, last, pay):   ##instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first.lower()+'.'+last.lower()+'@company.com'

    def fullname(self):
        return self.first+' '+self.last
    def raise_p(self):
        return int(self.pay*self.pay_raise)

emp_1=Employee('Pat', 'Nicoles', 40000)
emp_2=Employee('Daisy','Sandrea',45000)
emp_3=Employee('Kist','Klone',30000)

print(emp_1.email)
print(emp_2.fullname())
emp_3.pay_raise=1.2
print(emp_3.raise_p())






