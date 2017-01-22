""" This is my first python module to iterate a list of items.
Going good so far.
"""
import sys


def list_recursion(inputList, indent=False, level=0, op=sys.stdout):
    for listItem in inputList:
        if isinstance(listItem, list):
            list_recursion(listItem, indent, level+1, op)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=op)
            print(listItem, op)
