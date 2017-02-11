class Calculator(object):
    global_sum = 0

    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        total = self.value + other.value
        Calculator.global_sum = Calculator.global_sum + total
        return Calculator(total)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return "SUM: {}".format(self.value)

    def performAddition(self, *args):
        value = 0
        for each_value in args:
            value = value + each_value
        print("Perform Addition Result: {}".format(value))

    @staticmethod
    def global_result():
        val = Calculator.global_sum
        Calculator.global_sum = 0
        return val


def main():
    calc1 = Calculator(10)
    print(calc1)
    calc2 = Calculator(20)
    print(calc2)
    calc1.performAddition(10, 20)
    calc3 = calc1 + calc2
    print("calc1 + calc2 = calc3 : {}".format(calc3))
    print("calc3+ calc1 + calc2 = {}".format(calc3 + calc1 + calc2))
    print("sum([calc1, calc2, calc3]) = {}".format(sum([calc1, calc2, calc3])))
    print("Static global_result : {}".format(calc1.global_result()))


main()
