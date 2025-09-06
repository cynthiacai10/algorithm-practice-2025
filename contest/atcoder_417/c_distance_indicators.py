"""
AtCoder Beginner Contest 417
C Distance Indicators
https://atcoder.jp/contests/abc417/tasks/abc417_c

Yudanya
August 2th, 2025
"""

from collections import defaultdict

def distance_indicators(n, A):
    # i + A[i] == j - A[j]
    # i < j
    count = 0
    freq = defaultdict(int)

    for i in range(n):
        j_Aj = i - A[i]
        i_Ai = i + A[i]

        # (j - A[j])
        count += freq[j_Aj]
        # Compute current (i + A[i]) for future comparisons
        freq[i_Ai] += 1

    return count


def main():
    #n = 9
    #A = [3,1,4,1,5,9,2,6,5]
    n = int(input())
    A = list(map(int, input().split()))
    print(distance_indicators(n, A))


if __name__ ==  "__main__":
    main()


'''
def distance_indicators_klift(n, A):
    from collections import Counter
    # i + A[i] = j - A[j]

    # Count frequencies of j - A[j]
    right = Counter(j - A[j] for j in range(1, n))

    pair_count = 0
    for i in range(n - 1):
        # Before checking, reduce the count for i+1 - A[i+1] (which corresponds to j = i+1)
        right[i + 1 - A[i + 1]] -= 1

        pair_count += right[i + A[i]]

    return pair_count
'''