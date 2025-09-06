"""
AtCoder Beginner Contest 421
A - Misdelivery
https://atcoder.jp/contests/abc419/tasks/abc421_a

Cynthia
August 30th, 2025
"""

def main():
    # X, Y = map(int, input().split())
    n_room = int(input())
    room_people = [input() for i in range(n_room)]
    X, Y = input().split()

    if room_people[int(X)-1] == Y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()