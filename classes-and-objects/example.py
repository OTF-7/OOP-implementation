# creating a class.
class Employee:
    pass


# here we write the pass method because we are not going to work with it right now.


# creating an object.
emp1 = Employee()  # this simply says create a new object with the class "Employee".
# here we are using default python constructor for this class "Employee".

# setting attributes or instances(variables) to an object.
emp1.first = "Omar"
emp1.last = "Taha"
emp1.pay = 7000
# here each attributes are unique to other.

# we can now create a new object in this class too
emp2 = Employee()
emp2.first = "Essam"
emp2.last = "Morad"
emp2.pay = 2000

# printing from class
print(emp1.first + " " + emp1.last + " --> " + str(emp1.pay))
print(emp2.first + " " + emp2.last + " --> " + str(emp2.pay))

print("---------------------------------------------------------")
print("---------------------------------------------------------")


# lets create the same class using constructor.
class Employee1:
    def __init__(self, first, last,
                 pay):  # this is called a constructor.in python to make constructor we must use the keyword "__init__"
        self.first = first
        self.last = last  # in our constructor we are setting the instance variables or attributes.
        self.pay = pay
        self.email = first + "." + last + "@company.com"


# now we can pass value in our constructor(outside the class)
emp3 = Employee1("Amal", "Maher", 4000)
emp4 = Employee1("Ali", "Salim", 5000)
# in our object, attributes pass automatically.
# so we don't have to write any self argument.

print(emp3.first + " " + emp3.last + " --> " + str(emp3.pay) + f" [{emp3.email}]")
print(emp4.first + " " + emp4.last + " --> " + str(emp4.pay) + f" [{emp4.email}]")

"""Here what is happening behind the scene?
   self is a keyword.
   when we built constructors and an object like this one-
   python thinks that,
   self=emp1
   so "self.first" refers to"emp1.first"
   """

print("---------------------------------------------------------")
print("---------------------------------------------------------")


# but let ignore this bunch of code and go to our class and make a method which will handle this task easily.
class Employee2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):  # here note that, we need to add "self" argument to every method we want to add in the class.
        return f"{self.first} {self.last}"


emp5 = Employee2("Ahmed", "Ale", 3000)
emp6 = Employee2("Hossam", "Omar", 4000)

print(emp5.fullname())
print(Employee2.fullname(emp6))

print(emp5.fullname() + " --> " + str(emp5.pay) + f" [{emp5.email}]")
print(Employee2.fullname(emp6) + " --> " + str(emp6.pay) + f" [{emp6.email}]")
