# Question:
# 3510. Minimum Pair Removal to Sort Array II
#
# Given an array nums, you can perform the following operation any number of times:
#
# 1) Select the adjacent pair with the minimum sum in nums.
#    If multiple such pairs exist, choose the leftmost one.
# 2) Replace the selected pair with their sum.
#
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is non-decreasing if nums[i] >= nums[i-1] for all valid i.

import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Current values
        val = [int(x) for x in nums]

        # Doubly linked list via indices
        nxt = [i + 1 for i in range(n)]
        prv = [i - 1 for i in range(n)]
        nxt[-1] = -1
        prv[0] = -1

        # Marks removed indices
        removed = [False] * n

        # Count decreasing adjacent pairs
        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1

        # Already non-decreasing
        if bad == 0:
            return 0

        # Min-heap of (pairSum, leftIndex, rightIndex)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (val[i] + val[i + 1], i, i + 1))

        ops = 0

        # Perform forced merges until array becomes non-decreasing
        while pq:
            pair_sum, u, v = heapq.heappop(pq)

            # Skip invalid / outdated entries
            if removed[u] or removed[v] or nxt[u] != v:
                continue
            if val[u] + val[v] != pair_sum:
                continue

            ops += 1

            # Update bad count for pairs that disappear
            if val[u] > val[v]:
                bad -= 1

            l = prv[u]
            r = nxt[v]

            if l != -1 and val[l] > val[u]:
                bad -= 1
            if r != -1 and val[v] > val[r]:
                bad -= 1

            # Merge u and v into u
            val[u] = pair_sum
            removed[v] = True
            nxt[u] = r
            if r != -1:
                prv[r] = u

            # Add new adjacent pairs and update bad count
            if l != -1:
                if val[l] > val[u]:
                    bad += 1
                heapq.heappush(pq, (val[l] + val[u], l, u))

            if r != -1:
                if val[u] > val[r]:
                    bad += 1
                heapq.heappush(pq, (val[u] + val[r], u, r))

            # Stop as soon as the array becomes non-decreasing
            if bad == 0:
                return ops

        return ops


"""
Explanation:
- The operation order is forced: at every step we must merge the adjacent pair
  with the minimum sum (leftmost if tied).
- We model the array as a doubly linked list using index arrays (prv, nxt).
- A min-heap always gives the correct pair to merge in O(log n).
- Lazy deletion is used to skip outdated heap entries.
- We maintain `bad`, the number of positions where nums[i] > nums[i+1].
- Each merge updates only local relationships, so `bad` can be updated in O(1).
- As soon as `bad` becomes zero, the array is non-decreasing for the first time,
  and we stop.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""
