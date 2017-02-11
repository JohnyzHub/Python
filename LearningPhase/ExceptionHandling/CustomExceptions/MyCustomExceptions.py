class MyCustomException(Exception):
    def __init__(self, message, errorCode=0):
        super().__init__(message)
        self.errorCode = errorCode

    def getSeviority(self):
        if (self.errorCode > 2):
            return "Sevior"
        elif (self.errorCode == 1):
            return "Moderate"
        else:
            return "Ignorable"


class MyCustomExceptionOne(MyCustomException):
    def __init__(self, message, errorCode):
        super().__init__(message, errorCode)

    def getSeviority(self):
        val = super().getSeviority()
        return val


class MyCustomExceptionTwo(MyCustomException):
    def __init__(self, message, errorCode=1):
        super().__init__(message, errorCode)

    def getSeviority(self):
        return super().getSeviority()


class MyCustomExceptionThree(MyCustomException):
    def __init__(self, message, errorCode=3):
        super().__init__(message, errorCode)

    def getSeviority(self):
        return super().getSeviority()
