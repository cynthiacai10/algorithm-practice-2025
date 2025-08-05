"""
Timus
2012. About Grisha N.
https://acm.timus.ru/problem.aspx?space=1&num=2012

Yudanya
August 2th, 2025
"""

def about_grisha(f: int) -> bool:
    # f + the problems to solve in 2,3,4,5 hour
    total = f + 4*60//45
    return "YES" if total >= 12 else "NO"

def main():
    f = int(input())
    print(about_grisha(f))

if __name__ ==  "__main__":
    main()
