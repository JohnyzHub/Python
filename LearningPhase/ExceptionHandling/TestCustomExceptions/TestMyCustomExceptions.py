from ExceptionHandling.CustomExceptions.MyCustomExceptions import *


def testExceptions():
    a = input("Enter a number: ")
    try:
        if (a == 1):
            raise MyCustomExceptionOne("Testing custom exception one")
        elif (a == 2):
            raise MyCustomExceptionTwo("Testing custom exception two")
        else:
            raise MyCustomExceptionThree("Testing custom exception three")
    except (MyCustomExceptionOne, MyCustomExceptionTwo, MyCustomExceptionThree) as one:
        print("Exception - {} :: Message - {} :: Seviority - {}".format(one.__class__.__name__, one, one.getSeviority()))

    finally:
        print("Tested custom exceptions successfully!!")


testExceptions()
