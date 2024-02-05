# Questions, unable to answer

# - How many sorting algorithms are there?

''' 
Create a class with a constructor which initializes a limit variable.
create a method to print limit(say. 10) numbers, 
whenever the method is called it should print 10 numbers
eg. first call => print 1 to 10
    second call => print 11 to 20
'''

class Myclass:
    start = 1    
    def __init__(self,limit):
        self.limit = limit

    def output(self):
        for _ in range(self.limit):
            print(self.start)
            self.start += 1
        print()

obj = Myclass(10)
obj.output()
obj.output()

obj.output()