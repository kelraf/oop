
class Employee():

    amount_to_raice = 1.05
    num_of_emp = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + lastname + "@gmail.com"

        Employee.num_of_emp += 1


    def talk(self):
        return "My name is {} {} and I earn {} per month. For more information you can email me {}".format(self.firstname, self.lastname, self.pay, self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.amount_to_raice)


    @classmethod
    def set_raise_amount(cls, amount):
        cls.amount_to_raice = amount

print(Employee.num_of_emp)

emp_1 = Employee("Kelvin", "Kingara", 60000)
emp_2 = Employee("Juma", "Kenge", 50000)
emp_3 = Employee("Juma", "Kenge", 50000)


class Secretary(Employee):
    amount_to_raice = 1.10

    def __init__(self, firstname, lastname, pay, role):
        super().__init__(firstname, lastname, pay)
        self.role = role
        
sec_1 = Secretary("Kelvin", "Kingara", 60000, "role1")
sec_2 = Secretary("Juma", "Kenge", 50000, "role1")
sec_3 = Secretary("Juma", "Kenge", 50000, "role1")


class Manager(Employee):

    pass



#Employee.raise_amount = 1.06

#emp_1.raise_amount = 1.06

print(sec_1.__dict__)

Employee.set_raise_amount(1.07)
sec_1.apply_raise()
print(sec_1.talk())
print(Employee.amount_to_raice)
print(sec_1.amount_to_raice)
print(sec_3.amount_to_raice)
print(Employee.num_of_emp)
print(isinstance(sec_1, Employee))
# print(help(Secretary))