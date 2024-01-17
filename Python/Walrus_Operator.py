"""Learning about the Walrus operator in Python 3.8 and above."""

# It allows you to assign a value to a variable within an expression.

if __name__ == "__main__":

    # In the print() function
    print(a := False)

    # In the While loop : Example 1
    numbers = [1, 2, 3, 4, 5]

    while (n := len(numbers)) > 0:
        print(numbers.pop(), end=", ")

    # In the While loop : Example 2
    foods = list()

    print()
    while (food := input("what food do you like? : ")) != "quit":
        foods.append(food)
    