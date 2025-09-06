"""
AtCoder Beginner Contest 418
A - I'm a teapot
https://atcoder.jp/contests/abc418/tasks/abc418_a

Cynthia
August 9th, 2025
"""

def main():
    # Determine whether str is a string that ends with tea.
    n = int(input())
    s = input()
    if n < 3:
        print("No")
    else:
        if s[-3] == 't' and s[-2] =='e' and s[-1] == 'a':
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()