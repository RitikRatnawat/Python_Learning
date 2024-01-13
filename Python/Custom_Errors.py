"""Learning about the Custom errors in Python."""

# Custom Errors are user-defined exceptions. They provide a way to raise and handle specific types

class RangeError(Exception):
    """Custom Exception for Verifying number is in range.""" 
    pass
    

number  = int(input("Enter a number between 1-100 (inclusive) : "))

if not 1 <= number <= 100:
    raise RangeError(str(number) + " not in range 1-100.")