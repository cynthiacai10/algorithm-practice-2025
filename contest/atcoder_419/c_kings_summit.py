"""
AtCoder Beginner Contest 419
C - King's Summit
https://atcoder.jp/contests/abc419/tasks/abc419_c

Cynthia
August 16th, 2025
"""

import math


def main():
    input_count = int(input())
    rows, cols = [], []
    for _ in range(input_count):
        r, c = map(int, input().split())
        rows.append(r)
        cols.append(c)

    #test1 = [[2,5,8], [3,1,1]] # -> 3
    #test2 = [[6,6,6,6,6], [7,7,7,7,7]] # -> 0
    #test3 = [[91, 53, 32, 14, 49, 28], [86, 97, 32, 9, 85, 26]] # -> 44

    t_row = math.ceil((max(rows) - min(rows)) / 2)
    t_col = math.ceil((max(cols) - min(cols)) / 2)
    print(max(t_row, t_col))


if __name__ == '__main__':
    main()