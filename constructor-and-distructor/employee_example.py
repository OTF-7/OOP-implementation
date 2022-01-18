class Employee:

    # Initializing
    def __init__(self, name):
        self.name = name
        print(f'Hiring new employee ({self.name})')

    # Calling destructor
    def __del__(self):
        print(f"{self.name} was kicked off (fired)")


def hire_employee():
    name = input("Enter your name > ")
    emp = Employee(name)
    return emp


print('Calling Create_obj() function...')
emp = hire_employee()
del emp

