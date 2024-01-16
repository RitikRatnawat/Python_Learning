"""Learning about the Time module in Python."""

import time

def sum_using_while():
    """Sum from 1 to 50000 using While loop"""
    ans = 0
    i = 1

    while i <= 50000:
        ans = ans + i
        i = i + 1

    return ans

def sum_using_for():
    """Sum from 1 to 50000 using For loop"""
    ans = 0
    i = 1

    for i in range(1, 50001):
        ans = ans + i
        i = i + 1

    return ans


if __name__ == "__main__":
    print()
    start_time = time.time()
    result = sum_using_while()
    print(f"Time taken to calculate sum from 1-50000 using While Loop is {time.time() - start_time}")
    print(f"Result = {result}\n")

    # Pausing execution for 5 Seconds
    time.sleep(5)

    start_time = time.time()
    result = sum_using_for()
    print(f"Time taken to calculate sum from 1-50000 using For Loop is {time.time() - start_time}")
    print(f"Result = {result}\n")

    # Pausing execution for 5 Seconds
    time.sleep(5)

    # time.localtime() : Gives a time tuple with all details
    # time.strftime() : Formatting time in specified format
    t = time.localtime()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
    print(f"Current time : {formatted_time}\n")
