class Parent:
    name = "Father"

    def num(self):
        print(1)


class Child(Parent):
    # overriding variable
    name = "Son"

    # overriding num() method in the child class
    def num(self):
        print(0)


object_P = Parent()
print(object_P.name)
object_P.num()

object_H = Child()
print(object_H.name)
object_H.num()

print("---------------------------------------------------------")
print("---------------------------------------------------------")

# here we are using the same method and variable for 2 different class
# and they are handling each class separately which is polymorphism


# overloading
# in python we can define a method in such a way that there are multiple ways to call it.
# if we are given a single method or function, we can specify the number of parameters our self.
class Human:
    def hello(self, country=None):
        if country is None:
            print("Hello")
        elif country == "ENGLAND":
            print("Hello!")
        elif country == "GERMANY":
            print("Gutan Tag!")
        elif country == "FRANCE":
            print("Bonjour!")
        elif country == "MEXICO":
            print("Ola Amigo!")
        elif country == "INDIA":
            print("Namaste!")
        else:
            print("Hey!")


obj = Human()
obj.hello("MEXICO")

obj_2 = Human()
obj_2.hello("FRANCE")

print("---------------------------------------------------------")
print("---------------------------------------------------------")

# here hello is the same method but it will work differently depending on the arguements.
# we can do polymorphism with this overloading too.


# there is another type of overloading which is operator overloading.
# we can also create our own class and change the functionality of the add(+) operator.
class Special:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value * other.value
        # changing the behaviour of + method (making it *)


num_1 = Special(100)
num_2 = Special(20)

print(num_1 + num_2)
print(67 + 89)
print("Good " + "Boy")
