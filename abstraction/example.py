from abc import ABC, abstractmethod


class Configure(ABC):
    @abstractmethod
    def display(self):
        pass


class Mechanic(Configure):
    def display(self):
        print("this is display method for Mechanic")
        super().display()


m = Mechanic()
m.display()


class Configure2(ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Mechanic2(Configure2):
    def engine(self):
        print("this is engine method for Mechanic2")

    def color(self):
        pass


class SubMechanic2(Mechanic2):
    def color(self):
        print("this is abstract color method form a subclass of mechanic2")
        super().color()


m3 = SubMechanic2()
m3.engine()
m3.color()


class Cal(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass


class C(Cal):
    def __init__(self, value):
        super().__init__(value)

    def add(self):
        return self.value + 100

    def sub(self):
        return self.value - 10


obj = C(100)
print(obj.add())
print(obj.sub())
