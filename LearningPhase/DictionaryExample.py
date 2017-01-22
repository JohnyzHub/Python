from Utility.SanitizeData import sanitize


def dictionaryExample():
    file_loc = "C:\Workspaces\Workspace-Python" \
                "\LearningPhase\hfpy_ch5_data\sarah.txt"

    try:
        with open(file_loc) as file_sarah:
            readLine = file_sarah.readline().strip().split(',')
            print("readLine: {}".format(readLine))
    except IOError as ioError:
        print("Error in opening file.")
        return

    # dcit_sarah is the dictionary with keys name, dob and times
    dict_sarah = {"name": readLine.pop(0), "dob": readLine.pop(0),
                  "times": sanitize(readLine)}

    print("{}'s top 3 times {}".format(dict_sarah["name"],
                                       dict_sarah["times"][0:3]))


dictionaryExample()
