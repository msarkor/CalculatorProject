def Addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b


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




