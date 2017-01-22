def sanitize(inputList):
    if isinstance(inputList, list):
        newList = []
        for each_data in inputList:
            if ':' in each_data:
                splitter = ':'
            elif '-' in each_data:
                splitter = '-'
            else:
                splitter = '.'
            (mins, sec) = each_data.strip().split(splitter)
            newList.append(mins+"."+sec)

        resultSet = sorted(set(newList), reverse=True)
        print("Sanitized Data {}".format(resultSet))
        return resultSet
