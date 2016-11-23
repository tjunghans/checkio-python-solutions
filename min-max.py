#!/usr/bin/python

import myassert


def min(arg1, *args, **kwargs):
    modifier = None
    for key in kwargs:
        modifier = kwargs[key]
    if type(arg1) is str:
        items = list(arg1)
    elif type(arg1) is list:
        items = arg1
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

myassert.ok(min(2,3), 2)
myassert.ok(min(3,3), 3)
myassert.ok(min(4,3), 3)
myassert.ok(min(5,4,3), 3)
myassert.ok(min('hello'), 'e')
myassert.ok(min(2.2, 5.6, 5.9, key=int), 5.6, "Two maximal items")
myassert.ok(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])


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

myassert.ok(max(2,3), 3)
myassert.ok(max(3,3), 3)
myassert.ok(max(4,3), 4)
myassert.ok(max(3,4,5), 5)
myassert.ok(max('hello'), 'o')
