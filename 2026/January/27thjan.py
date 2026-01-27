# Question:
# 3650. Minimum Cost Path with Edge Reversals
#
# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1.
# Each edge [u, v, w] represents a directed edge u -> v with cost w.
#
# Each node has a switch usable at most once:
# - When you arrive at node u, you may reverse ONE incoming edge (x -> u)
#   into (u -> x) and immediately traverse it.
# - Traversing a reversed edge costs 2 * w.
# - The reversal is valid only for that single move.
#
# Return the minimum cost to travel from node 0 to node n - 1.
# If it is not possible, return -1.

from typing import List
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        # For every edge u -> v with cost w:
        #   - normal move: u -> v (cost w)
        #   - reverse move: v -> u (cost 2*w)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        # Dijkstra's algorithm
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]


"""
Explanation:

Key Insight:
- Each node’s switch is independent and can be used once.
- In a shortest-path context, revisiting a node at a higher cost is never optimal,
  so no path will benefit from using the same node’s switch more than once.
- Therefore, we do NOT need to track switch usage as state.

Graph Transformation:
For each original edge:
    u -> v (cost w)
we add:
    u -> v (cost w)       # normal traversal
    v -> u (cost 2 * w)   # reversed traversal using v's switch

After this transformation, the problem reduces to a standard shortest path problem.

Algorithm:
- Build the transformed graph.
- Run Dijkstra from node 0.
- Return the shortest distance to node n - 1.

Time Complexity:
O((n + m) log n)

Space Complexity:
O(n + m)
"""
