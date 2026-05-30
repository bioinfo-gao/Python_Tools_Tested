#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    def __init__(self, a, b):         #  << ===================== constructor
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)               # < ========================== generator
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(55, 89)
for r in f.series():
    if r > 1000: break    
    print(r, end=' ')

