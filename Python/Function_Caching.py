"""Learning about the Function Caching in Python."""

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fib(n):
    """Function to calculate the Fibonacci Series Number."""

    time.sleep(2)

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)



if __name__ == "__main__":

    start_time = time.time()
    fib(10)
    print(f"\nTime Taken to calculate to Fibonacci Series number at 10th position is {time.time() - start_time} seconds")

    start_time = time.time()
    fib(20)
    print(f"Time Taken to calculate to Fibonacci Series number at 20th position is {time.time() - start_time} seconds\n")

    print("\nAfter the Function Caching")
    print("----------"*5, "\n")
    start_time = time.time()
    fib(10)
    print(f"Time Taken to calculate to Fibonacci Series number at 10th position is {time.time() - start_time} seconds")

    start_time = time.time()
    fib(20)
    print(f"Time Taken to calculate to Fibonacci Series number at 20th position is {time.time() - start_time} seconds\n")
    