from MyKrazyListor import list_recursion


def printListItems():
    myList = ["Movie1", 1983, "Movie2", "Movie3",
              ["Movie4", 2001, ["Movie5", "Movie6", 2010, ["Movie7", 2020]]]]
    print("With Default values")
    list_recursion(myList)
    print("With true Level=1")
    list_recursion(myList, True, 1)
    print("With false level 0")
    list_recursion(myList, 0)
