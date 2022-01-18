class Trainee:

    def __init__(self, name, age):
        # public data members
        self.trainee_name = name
        self.trainee_age = age

    # public member function
    def display_age(self):
        # accessing public data member
        print("Age: ", self.trainee_age)


# creating object of the class
obj = Trainee("Omar Taha", 22)

# accessing public data member
print("Name: ", obj.trainee_name)

# calling public member function of the class
obj.display_age()
