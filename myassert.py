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


def ok(expression, expected, *args):
    message = ''
    if len(args) > 0:
        message = ' ' + args[0]

    if expression == expected:
        print bcolors.OKGREEN +  'Pass' + bcolors.ENDC
    else:
        print bcolors.FAIL +  'Fail:' \
            + ' is ' + str(expression) + ', should be ' + str(expected) \
            + message + bcolors.ENDC