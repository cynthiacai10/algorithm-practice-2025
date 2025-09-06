"""
AtCoder Beginner Contest 418
B - You're a teapot
https://atcoder.jp/contests/abc418/tasks/abc418_b

Cynthia
August 9th, 2025
"""

def main():
    s = input()

    n = len(s)
    max_rate = 0
    for i in range(n-2):
        count_t = 0
        if s[i] == 't':
            for j in range(i, n): 
                if s[j] == 't':
                    count_t += 1
                    if count_t >= 3:
                        length = j - i + 1
                        rate = (count_t-2)/(length-2)
                        max_rate = max(rate, max_rate)
    print(max_rate)

    
if __name__ == "__main__":
    main()