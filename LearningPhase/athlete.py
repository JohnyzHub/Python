from Utility.SanitizeData import sanitize


class AtheletCls:
    def __init__(self):
        pass
    '''
    def __init__(self, a_name, a_dob, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    '''
    def topThree(self):
        '''
        if hasattr(self, 'times'):
            print("{}'s top three times {}"
                  .format(self.name, self.times[0:3]))
        '''
        try:
            if len(self.times) > 0:
                print("{}'s top three times {}"
                      .format(self.name, self.times[0:3]))
        except AttributeError as atrErr:
            print(atrErr)

    def parseDataFile(self, a_file=''):
        try:
            with open(a_file) as athlete_file:
                athlete_line = athlete_file.readline().strip().split(',')
                print(athlete_line)
        except IOError as ioError:
            print("Error while opening file {}".format(str(ioError)))
            return

        self.name = athlete_line.pop(0)
        self.dob = athlete_line.pop(0)
        self.times = sanitize(athlete_line)
