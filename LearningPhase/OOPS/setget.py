class Rectangle:
    def __init__(self):
        pass

    @property
    def height(self):
        print("Returning height property")
        return self.__height

    @height.setter
    def height(self, value):
        print("Inside height setter")
        if value.isdigit():
            if int(value) > 0:
                self.__height = value
            else:
                print("Not a number: {}".format(value))
        else:
            print("Not a number: {}".format(value))

    @property
    def width(self):
        print("Returning width property")
        return self.__width

    @width.setter
    def width(self, value):
        print("Inside width setter")
        if value.isdigit():
            if int(value) > 0:
                self.__width = value
            else:
                print("Not a number: {}".format(value))
        else:
            print("Not a number: {}".format(value))

    def getArea(self):
        print("Inside getArea")
        hasHeight = hasattr(self, "height")
        hasWidth = hasattr(self, "width")
        if hasattr(self, "height") and hasattr(self, "width"):
            try:
                area = int(self.__height) * int(self.__width)
            except RuntimeError as error:
                print("Unable to get area: ".format(error))
            return area
        else:
            print("Some or all required attributes not available height:{} and width:{}".format(str(hasHeight),
                                                                                                str(hasWidth)))


def main():
    rect = Rectangle()
    height = input("Enter height:")
    rect.height = height
    width = input("Enter width: ")
    rect.width = width
    print("Area : {}".format(rect.getArea()))


main()
