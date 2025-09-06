"""
Delft Algorithm Programming Contest 2024
H - Human Pyramid
https://open.kattis.com/problems/humanpyramid

Cynthia
September 6, 2025
"""

def main():
    n = int(input())
    people = 0
    row = 1
    while True:
        people += row
        if people > n:
            break
        row += 1
    print(row-1)


if __name__ == "__main__":
    main()