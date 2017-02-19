from random import randint

print([(x * 2) for x in range(1, 15)])
print([x for x in range(1, 15) if (x % 2 == 0)])
print([i ** 2 for i in range(1, 50) if (i % 8 == 0)])


# print([x for x in [i for i in range(1, random(1, 10000))]])

class MyListItrFunc:
    def diviBy9(self):
        x = []
        for i in range(1, 51):
            x.append(randint(1, 1000))

        print("Random Values: {}".format(x))
        print("This is with filter functionality")
        print(list(filter(lambda y: (y % 9 == 0), x)))
        print("This is with list comprehension")
        print([a for a in x if (a % 9 == 0)])
        print("This is with list comprehension")
        print([p for p in ([randint(1, 1001) for q in range(50)]) if (p % 9 == 0)])


def main():
    myfunc = MyListItrFunc()
    myfunc.diviBy9()


main()
