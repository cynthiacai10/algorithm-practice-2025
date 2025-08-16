"""
AtCoder Beginner Contest 419
B - Get Min
https://atcoder.jp/contests/abc419/tasks/abc419_b

Cynthia
August 16th, 2025
"""

def get_min(queries):
    balls = []
    for q in queries:
        if q == "2": # Remove and print the smallest ball
            smallest = balls.pop(0)
            print(smallest)

        else: # Insert ball x into the correct position
            _, target = q.split()
            target = int(target)

            i = 0
            while i < len(balls) and balls[i] < target:
                i += 1
            balls.insert(i, target)


def main():
    query_count = int(input())
    queries = []
    for i in range(query_count):
        queries.append(input())

    #queries = ["1 6", "1 7", "2", "1 1", "2"] # -> 6, 1
    #queries = ["1 5", "1 1", "1 1", "1 9", "2", "2", "1 2", "2"] # -> 1, 1, 2

    get_min(queries)


if __name__ == "__main__":
    main()