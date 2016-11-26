#!/usr/bin/python

import myassert


def safe_pawns(pawns):
    num_safe_pawns = 0
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if len(pawns) == 1:
        return 0
    for p in pawns:
        safe = False
        col = p[0]
        rank = int(p[1])
        if rank > 1:
            protectorRank = str(rank - 1)  # must be one less
            if cols.index(col) > 0:
                left = cols[cols.index(col) - 1] + protectorRank
                if left in pawns:
                    safe = True
            if not safe and cols.index(col) < 7:
                right = cols[cols.index(col) + 1] + protectorRank
                if right in pawns:
                    safe = True
            if safe:
                num_safe_pawns += 1
    return num_safe_pawns


"""Test Cases."""

myassert.ok(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), 6)
myassert.ok(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}), 1)
myassert.ok(safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]), 7)
myassert.ok(safe_pawns(["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"]), 0)
myassert.ok(safe_pawns(["e8"]), 0)
