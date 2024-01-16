"""Learning about the Access Modifiers in the Python."""

# Private Access Modifiers : add __ before any class or instance variable.
# Protected Access Modifiers : add _ before any class or instance variable.
# Public Access Modifiers : add _ before any class or instance variable.


class Employee:
    """Employee Class to implement access modifiers."""

    def __init__(self, name, age, salary):
        self.__name = name # Private Variable
        self.age = age # Public variable
        self._salary = salary # Protected variable


if __name__ == "__main__":
    print()
    emp = Employee("Employee1", 25, 25000)

    # Private Variable
    try:
        print(emp.__name) # Cannot be accessed directly.
    except AttributeError as e:
        print(f"Getting AttributeError while accessing private variable : {e}")

    # Can be accessed indirectly using Name mangling
    print(f"Employee Name : {emp._Employee__name}\n")


    # Protected variable can be accessed directly but convention used is the start with _
    print(f"Employee Salary : {emp._salary}\n")

    # Public variable is defined as normal variable convention
    print(f"Employee Age : {emp.age}\n")

