class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# making a subclass
class Developer(Employee):  # here we are using the parent class name in the brackets,
    pass  # to specify which parent class' functionality we want to inherit.


# here is our subclass doesn't have any code of its own.
# but this subclass will have all the attributes methods of our Employee class.

dev_1 = Employee("Ahmad", "Salim", 200)
dev_2 = Employee("Khaled", "Noor", 400)

print(dev_1.email)
print(dev_2.email)

# it will also work if we create our object in Developer subclass
dev_1 = Developer("Rami", "Adel", 200)
dev_2 = Developer("Baker", "Omer", 400)

print(dev_1.email)
print(dev_2.email)

"""Method resolution order:
    Developer
    Employee      
    builtins.object"""

# now we want to customize our subclass.
# and we are going to change the raise_amount for our developers.
# but first lets see what happens when we apply raise_amount function to our current developers.
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print("---------------------------------------------------------")
print("---------------------------------------------------------")


# lets say we want our developers to raise amount of 1.10
# we can do this by-
class Developer2(Employee):
    raise_amount = 1.10


dev_3 = Developer2("sergio", "ramos", 500)

print(dev_3.pay)
dev_3.apply_raise()
print(dev_3.pay)

# now python using our developer subclass raise amount instead of parent class raise amount.
dev_4 = Employee("gerath", "bale", 800)

print(dev_4.pay)
dev_4.apply_raise()
print(dev_4.pay)

print("---------------------------------------------------------")
print("---------------------------------------------------------")


class Developer3(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # here we don't need to write all the code like self.pay=pay etc.
        self.prog_lang = prog_lang


dev_5 = Developer3("luca", "modrich", 300, "ruby")
dev_6 = Developer3("neymar", "jr.", 900, "java")

print(dev_5.email)
print(dev_5.prog_lang)

print("---------------------------------------------------------")
print("---------------------------------------------------------")


# lets make a new subclass called manager.
class Manager(Employee):
    def __init__(self, first, last, pay,
                 employees=None):  # here we don't use empty list for our default employees value.
        super().__init__(first, last,
                         pay)  # because we should not pass any mutable datatype like empty list or dictionary.
        if employees is None:  # instead of that we use None and do some extra coding to make sure that our code is error free.
            self.employees = []
        else:
            self.employees = employees

    # add a employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # remove a employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print out the fullnames of employees
    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


man_1 = Manager("zinedin", "zidane", 100, [dev_1])

print(man_1.email)
man_1.add_emp(dev_2)
man_1.add_emp(dev_3)
man_1.remove_emp(dev_1)
man_1.print_emp()

# is instance will tell us if an object is an instance/object of a class.
print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))
# here we need to enter two arguement.
# first one is the instance and the second is the class.

# is subclass will tell us if it is a subclass of a class.
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

print(hasattr(Manager, "add_emp"))  # NOTE: we have to pass the name of the property in string.
# we can also use this method with object instead of class,
print(hasattr(man_1, "remove_emp"))


# Extra tip:
# types of inheritance:
# single:
# when a inheritance involves one child class and one parent class only.
# multiple:
# when a inheritance involves more than one parent class.
# multilevel:
# the child class acts as a parant class for another parent class.
# hierarchical:
# it involvs multiple hybrid inheritance form the same parent class. it spreads like a tree.
# hybrid:
# it involves more than one type of inheritance.

# code:
# single:
class Parent:
    def func1(self):
        print("A function from the parent class")


class Child(Parent):
    def func2(self):
        print("A function from the child class")


# multiple:
class Parent1:
    def func3(self):
        print("A function from the parent1 class")


class Parent2:
    def func4(self):
        print("A function from the parent2 class")


class Child1(Parent1, Parent2):
    def func5(self):
        print("A function from the child1 class")


# multilevel:
class Parent3:
    def func6(self):
        print("A function from the parent3 class")


class Child2(Parent3):
    def func7(self):
        print("A function from the child2 class")


class Child3(Child2):
    def func8(self):
        print("A function from the child3 class which is a of child2 class")


# hierarchical(basic):
class Parent4:
    def func6(self):
        print("A function from the parent4 class")


class Child4(Parent4):
    def func7(self):
        print("A function from the child4 class")


class Child5(Parent4):
    def func8(self):
        print("A function from the child5 class")


# hierarchical(hybrid):
class Parent5:
    def func9(self):
        pass


class Child6(Parent5):
    def func10(self):
        pass


class Child7(Parent5):
    def func11(self):
        pass


class Child8(Child6, Child7):
    def func12(self):
        pass
