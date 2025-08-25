"""
AtCoder Beginner Contest 420
A - What month is it?
https://atcoder.jp/contests/abc419/tasks/abc420_a

Cynthia
August 24th, 2025
"""

def main():
    X, Y = map(int, input().split())
    month = (X+Y) % 12
    if month == 0:
        month = 12
    print(month)


if __name__ == "__main__":
    main()