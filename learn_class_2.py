##employee profile with first name, last, pay, email
##
##generate an email address form the first and last name and @company.com suffix
##generate the full name as a method
import datetime ##for static method

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

    ##class method to change variable pay_raise

    @classmethod    #decorator
    def set_pay_raise(cls, percent):    #cls is conventional, just like self
        cls.pay_raise = percent

    ##as an alternative constructor
    ##if variables are gvn all together with a colon between, we can do this
    @classmethod
    def from_new_emp(cls, new_emp):
        first, last, pay = new_emp.split(':')
        return cls(first,last,pay)

    ##order in last,pay,first
    @classmethod
    def from_rearrange(cls, arrange):
        first, last, pay= arrange[2], arrange[0], arrange[1]
        return cls(first,last,pay)

    ##static method
    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday==6:
            return 'Weekend'
        return 'Weekday'



print(Employee.number_of_employees)


emp_1=Employee('Pat', 'Nicoles', 40000)
emp_2=Employee('Daisy','Sandrea',45000)
emp_3=Employee('Kist','Klone',30000)

print(emp_1.email)
print(emp_2.fullname())
emp_3.pay_raise=1.2
print(emp_3.raise_p())
print(Employee.number_of_employees)

#using the class method - var
Employee.set_pay_raise(1.1)
print(emp_2.raise_p())

##using classmethod as constructor
new_emp_str= 'Kate:Rivers:37000'
emp_4= Employee.from_new_emp(new_emp_str)
print(emp_4.email)

print(Employee.number_of_employees)

##arrange last pay first    ->  forst last pay
new_emp_arrange = ('Chilo',50000,'Dan')
emp_5=Employee.from_rearrange(new_emp_arrange)
print(emp_5.first)


##static method
my_date = datetime.date(2015,2,15)
print(Employee.is_weekday(my_date))



