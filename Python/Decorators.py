"""Learning about the decorators in the Python."""

# Decorator Function to modify another function.
def logs(func):
    """Decorator Function

    Args:
        func (User-defined Function): Function to be decorated.
    """

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned a result = {result}\n")

    return wrapper


@logs
def add(a, b):
    """Function to add two numbers."""
    return a + b

@logs
def product(a, b):
    """Function to multiply two numbers."""
    return a * b

@logs
def exponent(a, b):
    """Function to calculate exponent."""
    return a ** b


if __name__ == "__main__":
    print()
    add(1546, 2548)
    product(120, 54)
    exponent(24, 10)
