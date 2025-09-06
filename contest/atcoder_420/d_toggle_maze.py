"""
AtCoder Beginner Contest 420
D - Toggle Maze
https://atcoder.jp/contests/abc419/tasks/abc420_d

Cynthia
August 24th, 2025
"""

from collections import deque

def main():
    n_row, n_col = map(int, input().split())
    grid = [list(input()) for _ in range(n_row)]

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    can_go = {".", "S", "G", "?"}

    # find start
    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] == "S":
                start_r, start_c = r, c

    # BFS state: (row, col, switch_state)
    q = deque([(start_r, start_c, False)])
    visited = set([(start_r, start_c, False)])
    steps = 0

    while q:
        for _ in range(len(q)):
            r, c, switch = q.popleft()

            # check goal
            if grid[r][c] == "G":
                print(steps)
                return

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_row and 0 <= nc < n_col:
                    cell = grid[nr][nc]

                    if cell in can_go:
                        nswitch = switch if cell != "?" else not switch
                        state = (nr, nc, nswitch)
                        if state not in visited:
                            visited.add(state)
                            q.append(state)

                    elif cell == "o" and not switch:
                        state = (nr, nc, switch)
                        if state not in visited:
                            visited.add(state)
                            q.append(state)

                    elif cell == "x" and switch:
                        state = (nr, nc, switch)
                        if state not in visited:
                            visited.add(state)
                            q.append(state)

        steps += 1

    # no path found
    print(-1)


if __name__ == "__main__":
    main()