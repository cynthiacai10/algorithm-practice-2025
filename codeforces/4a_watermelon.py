"""
Codeforces
4a. Watermelon
https://codeforces.com/problemset/problem/4/A

Yudanya
August 2th, 2025
"""

def main():
    weight = int(input())
    print("YES") if weight %2 == 0 and weight > 3  else print("NO")
        

if __name__ == "__main__":
    main()