from athlete import AtheletCls


def athleteRun():
    file_loc = "C:\Workspaces\Workspace-Python" \
                "\LearningPhase\hfpy_ch5_data\sarah.txt"
    athlete = AtheletCls()
    athlete.parseDataFile(file_loc)
    athlete.topThree()


athleteRun()
