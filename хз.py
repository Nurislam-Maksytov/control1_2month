class User:
    def __init__(self, name, age, balance=0):
        self.name = name
        self._age = age
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не может быть отрицательным")
        else:
            self.__balance = value


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно денег")

    def get_role(self):
        return "User"


class Student(User):
    def __init__(self, name, age, balance, course):
        super().__init__(name, age, balance)
        self.course = course

    def get_role(self):
        return f"Student of {self.course} course"


class Teacher(User):
    def __init__(self, name, age, balance, subject):
        super().__init__(name, age, balance)
        self.subject = subject

    def get_role(self):
        return f"Teacher of {self.subject}"

s = Student("Ali", 18, 100, 2)
t = Teacher("Aida", 35, 200, "Math")

print(s.get_role())
print(t.get_role())

s.deposit(50)
print(s.balance)

s.withdraw(30)
print(s.balance)

