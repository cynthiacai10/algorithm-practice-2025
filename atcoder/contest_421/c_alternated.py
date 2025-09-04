"""
AtCoder Beginner Contest 421
C - Alternated
https://atcoder.jp/contests/abc419/tasks/abc421_c

Cynthia
August 30th, 2025
"""

def min_adjacent_swaps(posi, target) -> int:
    swaps = 0
    for i in range(len(posi)):
        swaps += abs(posi[i] - target[i])
    return swaps
    #return sum(abs(a - b) for a, b in zip(posi, target))


def main():
    N = int(input())
    S = input()

    # A's positions
    posi_a = [i for i in range(len(S)) if S[i] == 'A']
    target1 = [2*i for i in range(N)]        # A in even positions
    target2 = [2*i + 1 for i in range(N)]    # A in odd positions

    cost1 = min_adjacent_swaps(posi_a, target1)
    cost2 = min_adjacent_swaps(posi_a, target2)

    print(min(cost1, cost2))

if __name__ == "__main__":
    main()