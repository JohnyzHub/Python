import os


def reading_file():
    print(os.getcwd())
    if os.path.exists('LearningPhase/Text File.txt'):
        print("File found")
    else:
        print("File not found")
        return

    data = open('LearningPhase/Text File.txt')
    for each_line in data:
        print(each_line, end='')
    data.close()

    curr_dir = "C:\Python-Utils"
    os.chdir(curr_dir)
    data = open('SampleFile.txt')
    print("first line: {}".format(data.readline()))
    data.seek(0)
    master = []
    student = []
    for curr_line in data:
        # print(curr_line, end='')
        if curr_line.find(":") != -1:
            (role, text) = curr_line.split(":", 1)
            # print("{}:{}".format(role, text), end='')
            refindText = text.strip()
            if role == "Master":
                master.append(refindText)
            else:
                student.append(refindText)
        else:
            print(curr_line, end='')

    data.close()
    print("Master:{}".format(master), end="")
    print("")
    print("Student:{}".format(student), end="")

    try:
        master_file = open("MasterFile.txt", "w")
        student_file = open("StudentFile.txt", "w")
        print(master, file=master_file)
        test_file = open("test_file.txt")
        print(student, file=student_file)
    except IOError:
        print("")
        print("File Error")
    finally:
        master_file.close()
        student_file.close()
        test_file.close()


reading_file()
