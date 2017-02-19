class IterateString:
    def __init__(self, str="abcdefghijklmnopqrstuvwxyz"):
        self.str = str
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.str) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.str[self.index]


iterateString = IterateString("abcdefghij")
print("Method 1:")
for i in range(len(iterateString.str)):
    print(next(iterateString))

iterateString.index = -1
print("Method 2:")
for letter in iterateString:
    print(letter)


class CustomFebinacci:
    def __init__(self):
        self.firstIndex = 1
        self.secondIndex = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.result = self.firstIndex + self.secondIndex
        self.firstIndex = self.secondIndex
        self.secondIndex = self.result
        return self.result


customFebinacci = CustomFebinacci()
print("Febinacci Series:")
for i in range(10):
    print(next(customFebinacci))


def myFebinacci(aNumber):
    if aNumber <= 1:
        return 1

    if aNumber == 2:
        return 2

    return myFebinacci(aNumber - 1) + myFebinacci(aNumber - 2)


print("MyFebinacci: ")
for i in range(1,11):
    print(myFebinacci(i))
