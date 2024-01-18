"""Learning about the Generators in Python."""

def square_generator(n):
    """Generator to get square of numbers.

    Args:
        n (int): Range of the Squares

    Yields:
        int: Returns square of number
    """

    for i in range(1, n+1):
        yield i ** 2


if __name__ == "__main__":

    num = 1
    for sq in square_generator(10):
        print(f"Square of {num} is {sq}")
        num = num + 1