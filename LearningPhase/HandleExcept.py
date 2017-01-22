
def handle_except():
    myFile = "C:\Python-Utils\SampleFile.txt"
    try:
        data = open(myFile)
    except:
        print("File not Found")
        return

    for each_line in data:
        try:
            (role, statemt) = each_line.split(":", 1)
            print("{}:{}".format(role, statemt), end='')
        except:
            print(each_line, end='')
    data.close()


handle_except()
