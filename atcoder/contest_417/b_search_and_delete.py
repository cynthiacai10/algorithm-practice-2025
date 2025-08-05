"""
AtCoder Beginner Contest 417
B Search and delete
https://atcoder.jp/contests/abc417/tasks/abc417_b

Yudanya
August 2th, 2025
"""

from collections import Counter


def main():
    # Excellent (O(N + M))
    # fast lookup through hash map (counter)
    n, m = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    b_counter = Counter(b_arr)

    for num in a_arr:
        if b_counter[num] > 0:
            b_counter[num] -= 1
        else:
            print(num, end=" ")


if __name__ ==  "__main__":
    main()

"""
def method1():
    n, m= map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    for b in b_lst:
        if b in a_lst:
            a_lst.remove(b) # but only remove one a, but all b
 
    print(" ".join(a_lst))
"""