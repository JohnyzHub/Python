from random import randint

print([(x * 2) for x in range(1, 15)])
print([x for x in range(1, 15) if (x % 2 == 0)])
print([i ** 2 for i in range(1, 50) if (i % 8 == 0)])

multiDimension = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
print("MultiDimension column[1] - {}".format([col[1] for col in multiDimension]))
print("MultiDimension column[i] - {}".format([multiDimension[i][i] for i in range(len(multiDimension))]))

'''
LIST COMPREHENSIONS
'''


class MyListItrFunc:
    def diviBy9(self):
        x = []
        for i in range(1, 10):
            x.append(randint(1, 1000))

        print("Random Values: {}".format(x))
        print("This is with filter functionality")
        print(list(filter(lambda y: (y % 9 == 0), x)))
        print("This is with list comprehension")
        print([a for a in x if (a % 9 == 0)])
        print("This is with another way of list comprehension")
        print([p for p in ([randint(1, 1001) for q in range(50)]) if (p % 9 == 0)])


def main():
    myfunc = MyListItrFunc()
    myfunc.diviBy9()


main()

'''
GENERATORS
'''


def isPrime(num):
    if num <= 1:
        return False

    if num == 2:
        return False

    if num == 3:
        return True

    for i in range(2, int(num / 2) + 1):
        if (num % i == 0):
            return False
    return True


def getPrimeNums(num):
    if num <= 0:
        return

    for i in range(2, num):
        if (isPrime(i)):
            yield i


primeGenerator = getPrimeNums(50)
print("Prime Number: {}".format(next(primeGenerator)))
print("Prime Number: {}".format(next(primeGenerator)))
print("Prime Number: {}".format(next(primeGenerator)))
print("Prime Number: {}".format(next(primeGenerator)))

'''
Generator Expressions
'''
numSquare = (i * 2 for i in range(10))
print("numSquare First-{}".format(next(numSquare)))
print("numSquare Second-{}".format(next(numSquare)))
print("numSquare {}".format(list(numSquare)))
