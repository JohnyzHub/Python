import pickle
from pickle import PickleError


def pickle_test():
    file_loc = "C:\Python-Utils\Pickle_File.txt"
    try:
        with open(file_loc, "wb") as save_to_file:
            pickle.dump(["One", 1, "Two", 2, "Three", 3], file=save_to_file)

        with open(file_loc, "rb") as read_from_file:
            data_read = pickle.load(read_from_file)
            print(data_read)
    except PickleError as pickle_error:
        print("PickleError - {}".format(pickle_error))
    except IOError as io_error:
        print("IOError-{}".format(io_error))


pickle_test()
