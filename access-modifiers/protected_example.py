class Trainee:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _display_roll_and_branch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class ERP(Trainee):

    # constructor
    def __init__(self, name, roll, branch):
        Trainee.__init__(self, name, roll, branch)

    # public member function
    def display_details(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._display_roll_and_branch()


# creating objects of the derived class
obj = ERP("Omar Taha", 1706256, "Computer science")

# calling public member functions of the class
obj.display_details()
