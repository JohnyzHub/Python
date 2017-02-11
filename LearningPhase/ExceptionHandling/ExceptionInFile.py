#from ExceptionHandling import MyCustomException
#import ExceptionHandling.MyCustomException


def handle_except():

    myFile = "C:\Python-Utils\SampleFile.txt"
    try:
        data = open(myFile)
    except Exception as e:
        print("File not Found. Exception - {} :::: {} ".format(type(e).__name__, e))
        return

    for each_line in data:
        try:
            (role, statemt) = each_line.split(":", 1)
            print("{}:{}".format(role, statemt), end='')
        except:
            print(each_line, end='')
    data.close()


handle_except()
