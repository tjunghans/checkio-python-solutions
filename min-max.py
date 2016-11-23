#!/usr/bin/python

import myassert


def minmax(min, arg1, *args, **kwargs):

    key = kwargs.get("key", None)
    if type(arg1) is int or type(arg1) is float:
        items = [arg1]
    elif type(arg1) is list:
        items = arg1
    elif type(arg1) is bool:
        items = [int(arg1)]
    else:
        items = list(arg1)

    if len(args) > 0 and type(args[0]) is list:
        items = [items]

    res = items[0]

    for arg in args:
        items.append(arg)

    for x in items:
        if key:
            if (min and key(x) < key(res)) or (not min and key(x) > key(res)):
                res = x
        else:
            if (min and x < res) or (not min and x > res):
                res = x

    return res


def min(arg1, *args, **kwargs):
    return minmax(True, arg1, *args, **kwargs)


def max(arg1, *args, **kwargs):
    return minmax(False, arg1, *args, **kwargs)

myassert.ok(min(2,3), 2)
myassert.ok(min(3,3), 3)
myassert.ok(min(4,3), 3)
myassert.ok(min(5,4,3), 3)
myassert.ok(min('hello'), 'e')
myassert.ok(min(2.2, 5.6, 5.9, key=int), 2.2, "One minimal items")
myassert.ok(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0])
myassert.ok(min(abs(i) for i in range(-10, 10)), 0, 'should be 0')
myassert.ok(min((9,)), 9, 'should be 9')
myassert.ok(min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum), [1, 2, 3])
myassert.ok(min(True, False, -1, key=lambda x: not x), True)

myassert.ok(max(2,3), 3)
myassert.ok(max(3,3), 3)
myassert.ok(max(4,3), 4)
myassert.ok(max(3,4,5), 5)
myassert.ok(max('hello'), 'o')
myassert.ok(max(2.2, 5.6, 5.9, key=int), 5.6, "Two maximal items")
myassert.ok(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [3, 4])
myassert.ok(max(range(6)), 5)
myassert.ok(max(abs(i) for i in range(-10, 10)), 10)
myassert.ok(max((9,)), 9, 'should be 9')
myassert.ok(max([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum), [5, 6])
myassert.ok(max(True, False, -1, key=lambda x: not x), False)
