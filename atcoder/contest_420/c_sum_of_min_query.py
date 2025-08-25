"""
AtCoder Beginner Contest 420
C - Sum of Min Query
https://atcoder.jp/contests/abc419/tasks/abc420_c

Cynthia
August 24th, 2025
"""

def main():
    n_number, n_query = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    queries = [input().split() for _ in range(n_query)]

    min_val = []
    min_sum = 0
    for i in range(n_number):
        smaller = min(A[i], B[i])
        min_val.append(smaller)
        min_sum += smaller

    for category, idx, new_val in queries:
        idx, new_val = int(idx)-1, int(new_val)
        if category == "A":
            A[idx] = new_val
        else:
            B[idx] = new_val
        new_min = min(A[idx], B[idx])
        min_sum += new_min - min_val[idx]
        min_val[idx] = new_min
        print(min_sum)
        

if __name__ == "__main__":
    main()
