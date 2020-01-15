class Calculator(object):

    def __init__(self, value=0):
        self.result = value

    def mul(self, x, y):
        self.result = (x * y)
        return self.result