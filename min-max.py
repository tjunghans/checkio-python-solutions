#!/usr/bin/python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ok(expression, expected):
    if expression == expected:
        print bcolors.OKGREEN +  "Pass" + bcolors.ENDC
    else:
        print bcolors.FAIL +  "Fail" + bcolors.ENDC


def min(arg1, *args, **kwargs):
    modifier = None
    for key in kwargs:
        modifier = key
    if type(arg1) is str:
        items = list(arg1)
    else:
        items = [arg1]
    minArg = items[0]
    for arg in args:
        items.append(arg)
    for x in items:
        if modifier:
            if modifier(x) < modifier(minArg):
                minArg = x
        else:
            if x < minArg:
                minArg = x
    return minArg

ok(min(2,3), 2)
ok(min(3,3), 3)
ok(min(4,3), 3)
ok(min(5,4,3), 3)
ok(min('hello'), 'e')
ok(min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])


def max(arg1, *args, **keys):
    if type(arg1) is str:
        items = list(arg1)
    else:
        items = [arg1]
    maxArg = items[0]
    for arg in args:
        items.append(arg)
    for x in items:
        if x > maxArg:
            maxArg = x
    return maxArg

ok(max(2,3), 3)
ok(max(3,3), 3)
ok(max(4,3), 4)
ok(max(3,4,5), 5)
ok(max('hello'), 'o')
