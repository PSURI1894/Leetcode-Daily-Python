# Question:
# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
#
# A node is called the deepest if it has the largest depth among all nodes in the tree.
# The subtree of a node is the tree consisting of that node and all its descendants.


class Solution:
    def subtreeWithAllDeepest(self, root):
        
        # DFS returns a pair: (deepest_depth_from_this_node, subtree_root)
        def dfs(node):
            if not node:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            # If left subtree is deeper, propagate it
            if left_depth > right_depth:
                return left_depth + 1, left_node

            # If right subtree is deeper, propagate it
            if right_depth > left_depth:
                return right_depth + 1, right_node

            # If both sides have equal depth,
            # current node is the smallest subtree containing all deepest nodes
            return left_depth + 1, node

        return dfs(root)[1]


# Explanation:
# This problem is best solved using a bottom-up DFS.
#
# Key idea:
# For every node, we want to know:
# 1) The maximum depth of its left subtree
# 2) The maximum depth of its right subtree
#
# DFS returns two things:
# - depth: maximum depth from this node downwards
# - node: the root of the smallest subtree containing all deepest nodes
#
# Logic:
# - If left subtree is deeper → deepest nodes lie entirely on the left
# - If right subtree is deeper → deepest nodes lie entirely on the right
# - If both depths are equal → deepest nodes are split across both sides,
#   so the current node is their lowest common ancestor (answer)
#
# This naturally gives us the smallest subtree containing all deepest nodes.
#
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack