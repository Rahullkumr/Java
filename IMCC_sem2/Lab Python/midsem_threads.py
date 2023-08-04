import threading

factorial = None
def calculate():
    def fact(num):
        if num in (0,1):
            return 1
        return num * fact(num - 1)


    no = 5
    global factorial
    factorial = fact(no)


def display():
    global factorial
    print(f"Factorial of 5 is: {factorial}")


t1 = threading.Thread(target=calculate)
t2 = threading.Thread(target=display)

t1.start()
t2.start()

t1.join()
t2.join()

print("Execution done")

print("This program uses various concepts like Multi Threading, inner fn, recursion, global variables and fstring")