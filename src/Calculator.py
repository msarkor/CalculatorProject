def Addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return float(b) / float(a)

def square(a):
    return a ** 2

def squareroot(a):
    return a ** (.5)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def Addition(self, a, b):
        self.result = Addition(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result



