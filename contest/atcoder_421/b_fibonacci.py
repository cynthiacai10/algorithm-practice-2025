"""
AtCoder Beginner Contest 421
B - Fibonacci Reversed
https://atcoder.jp/contests/abc419/tasks/abc421_b

Cynthia
August 30th, 2025
"""
def main():
    X, Y = map(int, input().split())
    a = [-1] * 10
    a[0], a[1] = X, Y
    for i in range(2, 10):
        a[i] = int(str(a[i-1] + a[i-2])[::-1])
    print(a[9])


if __name__ == "__main__":
    main()