"""
Delft Algorithm Programming Contest 2024
L - Lawful Limits
https://open.kattis.com/problems/lawfullimits

Cynthia
September 6, 2025
"""

import sys
import heapq
from collections import defaultdict

def edge_time(length, v1, v2, t_total, t_change):
    if t_total >= t_change:  # Use v2
        return length / v2
    else:
        t_slow_full = length / v1
        if t_total + t_slow_full <= t_change:  # Use v1
            return t_slow_full
        else:  # Use v1 and v2
            t_slow = t_change - t_total
            t_fast = (length - t_slow * v1) / v2
            return t_slow + t_fast


def main():
    rl = sys.stdin.readline
    n, m, t_change = map(int, rl().split())
    roads = [tuple(map(int, rl().split())) for _ in range(m)]

    # 1. Build adjacency list
    adj = defaultdict(list)
    for x, y, L, v1, v2 in roads:
        adj[x].append((y, L, v1, v2))
        adj[y].append((x, L, v1, v2))

    
    # 2. DP: store smallest arrival time for each node
    best_time = [float('inf')] * (n + 1)
    best_time[1] = 0.0

    # 3. Use BFS / priority queue to find quick paths
    heap = [(0.0, 1)] # (best_time, node)
    while heap:
        t_total, node = heapq.heappop(heap)
        if node == n:
            print(f"{best_time[n]:.10f}")
            return

        for nei, length, v1, v2 in adj[node]:
            # Compute time on this road
            t_road = edge_time(length, v1, v2, t_total, t_change)
            t_new = t_total + t_road
            if t_new < best_time[nei]:
                best_time[nei] = t_new
                heapq.heappush(heap, (t_new, nei))

    print(f"{best_time[n]:.10f}")


if __name__ == "__main__":
    main()