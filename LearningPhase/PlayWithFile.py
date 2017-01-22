import os


def play_with_file():
    file_loc = "C:\Python-Utils\play_with_file.txt"

    file_ref = ""
    try:
        file_ref = open(file_loc, "r")
        for each_line in file_ref:
            print(each_line, end="")
    except IOError as error:
        print("ex- {}".format(error))
    finally:
        if os.path.exists(file_loc):
            file_ref.close()
            os.remove(file_loc)
            print("File Deleted")
        else:
            print("No need to close the file")

    try:
        # Using 'With', python will take care to close the file.
        with open(file_loc, "w+") as file_ref:
            print("This is first line", file=file_ref)
            print("This is second line", file=file_ref)
            file_ref.seek(0)
            print(file_ref.readline(), end="")
            for each_line in file_ref:
                print(each_line, end="")
            print("Python will auto-close this file.")
    except IOError as error:
        print(error)
        print("ex-{}".format(error))

    if os.path.exists(file_loc):
        os.remove(file_loc)
        print("File deleted")


play_with_file()
