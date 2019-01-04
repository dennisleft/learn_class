##employee profile with first name, last, pay, email
##
##generate an email address form the first and last name and @company.com suffix
##generate the full name as a method


class Employee:

    ##class variable
    pay_raise = 1
    number_of_employees = 0


    def __init__(self, first, last, pay):   ##instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first.lower()+'.'+last.lower()+'@company.com'
        Employee.number_of_employees +=1
        ##to my understanding, we use Employee.number_of employees because
        ##to get the number of employees, we count the instances of the class

    def fullname(self):
        return self.first+' '+self.last
    def raise_p(self):
        return int(self.pay*self.pay_raise)

print(Employee.number_of_employees)


emp_1=Employee('Pat', 'Nicoles', 40000)
emp_2=Employee('Daisy','Sandrea',45000)
emp_3=Employee('Kist','Klone',30000)

print(emp_1.email)
print(emp_2.fullname())
emp_3.pay_raise=1.2
print(emp_3.raise_p())
print(Employee.number_of_employees)






