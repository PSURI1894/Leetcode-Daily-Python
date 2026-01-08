# Question:
# Given the root of a binary tree, the level of its root is 1,
# the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values
# of nodes at level x is maximum.


from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer_level = 1

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level

            level += 1

        return answer_level


# Explanation:
# We perform a level-order traversal (BFS) of the binary tree.
#
# For each level:
# - We calculate the sum of node values at that level.
# - If this sum is greater than the maximum sum seen so far,
#   we update the maximum sum and record the current level.
#
# Since we traverse levels from top to bottom,
# the first level with the maximum sum is automatically chosen,
# satisfying the "smallest level" requirement.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
