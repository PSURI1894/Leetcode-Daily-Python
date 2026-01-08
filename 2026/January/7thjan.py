# Question:
# Given the root of a binary tree, split the binary tree into two subtrees
# by removing exactly one edge such that the product of the sums of the
# two resulting subtrees is maximized.
#
# Return the maximum product of the subtree sums.
# Since the answer may be very large, return it modulo (10^9 + 7).
#
# Note: You must maximize the product before taking the modulo.


class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        subtree_sums = []

        # First DFS: compute subtree sums
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total = node.val + left_sum + right_sum
            subtree_sums.append(total)
            return total

        total_sum = dfs(root)

        max_product = 0
        for s in subtree_sums:
            max_product = max(max_product, s * (total_sum - s))

        return max_product % MOD


# Explanation:
# The idea is to try cutting every possible edge in the tree.
# When we cut an edge, the tree splits into:
# - one subtree with sum = s
# - the remaining tree with sum = total_sum - s
#
# The product for this cut is:
# s * (total_sum - s)
#
# Steps:
# 1) Use DFS to compute the sum of every subtree.
#    While doing this, store each subtree sum in a list.
# 2) The total sum of the tree is the sum at the root.
# 3) For each subtree sum s, compute the product:
#       s * (total_sum - s)
#    and keep track of the maximum product.
# 4) Return the maximum product modulo (10^9 + 7).
#
# Important:
# - We compute the maximum product first.
# - The modulo is applied only at the very end, as required.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
