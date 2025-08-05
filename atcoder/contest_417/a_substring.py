"""
AtCoder Beginner Contest 417
A Substring
https://atcoder.jp/contests/abc417/tasks/abc417_a

Yudanya
August 2th, 2025
"""

def main():
    n, a, b = map(int, input().split())
    string = str(input())
    print(string[a:(n-b)])

if __name__ ==  "__main__":
    main()