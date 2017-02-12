from functools import reduce

'''
Exercise with args and kwargs
'''


def parseArgs(*args, **kwargs):
    print("args.count={}, args[0]={}".format(len(args), args[0]))
    for count, object in enumerate(args):
        print("{}:{}".format(count, object))

    print("kwargs.count={}".format(len(kwargs)))
    for name, value in kwargs.items():
        print("{}:{}".format(name, value))


parseArgs(10, 20, 30)
parseArgs("Johny", "Basha", "Shaik", apple="fruit", cabbage="vegetable")
shopping_list = {"fruit": ["apple", "banana", "oranges"], "vegetables": ["cabbage", "carrot", "okra"]}
parseArgs(shopping_list["fruit"], shopping_list["vegetables"], apple="fruit", cabbage="vegetable")

'''
Exercise with decorators and nested functions
'''


def multiply_validator(outerInput):
    def perform_multiply(innerInput):
        return innerInput * outerInput

    return perform_multiply


one_func = multiply_validator(5)
print("5 * 10 = ", one_func(10))
print("5 * 20 = ", one_func(20))


def division_validator(func):
    def perform_validation(a, b):
        if a >= 0 and b > 0:
            return func(a, b)
        else:
            print("Invalid arguments for division.")
            return

    return perform_validation


@division_validator
def perform_division(a, b):
    print("{}/{} = {}".format(a, b, (a / b)))


perform_division(25, 5)

func_division = division_validator(perform_division)
func_division(30, 5)

'''
Function annotations
'''


def functionAnnotate(name: str, age: int, weight: float) -> str:
    return print("{} is {} years old and weighs {}".format(name, age, weight))


functionAnnotate("Johny", 34, 170.00)

'''
Lambda Functions
'''
print("-------------------Lamda ---------------------------")
print("Lamda::Map")
print(list(map(lambda x: x ** 2, range(0, 4))))
print(list(map(lambda x, y: (x ** 2 + y ** 2), range(0, 4), range(0, 4))))


def power(x):
    return x ** 2


def cube(x):
    return x ** 3


print("Lambda::Map with power(^2) and cube(^3)")
for each_item in range(0, 5):
    result = map(lambda x: x(each_item), [power, cube])
    print(each_item, list(result))

'''
Filter
'''

print("Lambda::Filter -> 9 divisibles in (0 to 100) are",
      list(filter(lambda x: (x > 0) and (x % 9 == 0), range(0, 100))))

'''
REDUCE
'''
print("Lambda::Reduce -->", reduce((lambda x, y: x + y), range(0, 6)))
