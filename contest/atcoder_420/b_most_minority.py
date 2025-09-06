"""
AtCoder Beginner Contest 420
B - Most Minority
https://atcoder.jp/contests/abc419/tasks/abc420_b

Cynthia
August 24th, 2025
"""

def main():
    n_people, n_votes = map(int, input().split())
    votes = [input() for _ in range(n_people)] # 2D matrix, row people, column vote

    # iterate each column (vote) and compute scores
    scores = [0] * n_people
    for col in range(n_votes):
        sum = 0
        idx_1, idx_0 = [], []
        for row in range(n_people):
            if votes[row][col] == "1":
                sum += 1
                idx_1.append(row)
            else:
                idx_0.append(row)
        if sum > (n_people/2): # 0 is minority
            for i in idx_0:
                scores[i] += 1
        else:
            for i in idx_1:
                scores[i] += 1
    
    # find people with the highest scores
    max_score = max(scores)
    indices = [i+1 for i, x in enumerate(scores) if x == max_score] # 1-index!!
    print(*indices)


if __name__ == "__main__":
    main()