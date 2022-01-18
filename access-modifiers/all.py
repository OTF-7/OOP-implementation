class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def display_public_members(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _display_protected_members(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __display_private_members(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def access_private_members(self):
        # accessing private member function
        self.__display_private_members()


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def access_protected_members(self):
        # accessing protected member functions of super class
        self._display_protected_members()


# creating objects of the derived class
obj = Sub("Omar", 7, "Taha")

# calling public member functions of the class
obj.display_public_members()
obj.access_protected_members()
obj.access_private_members()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)
