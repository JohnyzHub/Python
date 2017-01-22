def readDataFromFiles():
    file_james = 'C:\Workspaces\Workspace-Python' \
                 '\LearningPhase\hfpy_ch5_data\james.txt'

    # Reading each line from the file
    with open(file_james) as james_file:
        data = james_file.readline()
        print("James Raw - {}".format(data))

    james_data = data.strip().split(',')
    print("James Stripped - {}".format(james_data))

    james_sorted = sorted(james_data)
    print("James Sorted - {}".format(james_sorted))

    james_sanitized = []
    # Reading each value from the object
    for each_value in james_sorted:
        james_sanitized.append(sanitize(each_value))
    print("Sanitized James : {}".format(james_sanitized))

    # Better way of doing the above for loop code.
    # Using Data comprehension.
    efficient_sanity_james = [sanitize(each_t) for each_t in james_sorted]
    print("Efficiently Sanitized James: {}".format(efficient_sanity_james))

    # Removing Duplicates
    unique_james = []
    for each_data in efficient_sanity_james:
        if each_data not in unique_james:
            unique_james.append(each_data)
    print("Remving Duplicates: {}".format(unique_james))

    unique_sorted = sorted(unique_james)
    print("Sanitized Unique Ascending James : {}".format(unique_sorted))

    descend_sorted = sorted(unique_james, reverse=True)
    print("Sanitized Unique Descending James : {}".format(descend_sorted))

    print("Printing top 3 numbers from the list: {}".format(unique_sorted[0:3]))

    # Simplest way of removing duplicates
    print("Remving duplicates and sorting using SET: {}".format(sorted(set([sanitize(each_row) for each_row in james_data]))))


def sanitize(temp_String):
    if '-' in temp_String:
        splitter = '-'
    elif ':' in temp_String:
        splitter = ':'
    else:
        splitter = '.'
    (mins, sec) = temp_String.split(splitter)
    return (mins+'.'+sec)


readDataFromFiles()
