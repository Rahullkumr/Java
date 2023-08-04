# 4 b
# Write a multithreading program, where one thread prints square of a
# number and another thread prints factorial of a number.
# Also display the total time taken for the execution.

import threading
import time as t


def square():
    print("Square of 5 is: ", 5*5)


def factorial():
    def fact(n):
        if n in (0, 1):
            return 1
        return n * fact(n - 1)

    print("Factorial of 5 is: ", fact(5))


start_time = t.time()

t1 = threading.Thread(target=square)
t2 = threading.Thread(target=factorial)

t1.start()
t2.start()

t1.join()
t2.join()
end_time = t.time()

time_taken = end_time - start_time
print("Execution done")
print(f"Time taken for execution: {time_taken} seconds")
