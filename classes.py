class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@nelson.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def raise_(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise(cls, amt):
        cls.raise_amount = amt

class Developer():
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee,Developer):
    pass


man = Manager('Nelson', 'Wisdom', 40000, 'Python')
employee2 = Employee('Nelson', 'Wisdom', 30000)
#print(help(Developer))
# print(dev.email)
# print(dev.fullname())
print(man.lang)

# print(dev.pay)
# #employee2.raise_()
#
# print(employee2.pay)

