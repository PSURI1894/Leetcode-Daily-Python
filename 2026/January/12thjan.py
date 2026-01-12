# Question:
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
# You need to visit all the points in the given order.
#
# In 1 second, you can:
# - Move vertically by 1 unit, or
# - Move horizontally by 1 unit, or
# - Move diagonally by 1 unit (i.e., move 1 unit vertically and 1 unit horizontally).
#
# Return the minimum time in seconds to visit all the points in order.


class Solution:
    def minTimeToVisitAllPoints(self, points):
        total_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            # Time needed is the maximum of horizontal and vertical distance
            total_time += max(dx, dy)

        return total_time


# Explanation:
# The key observation is that diagonal movement allows us to reduce both
# x and y distance at the same time.
#
# To move from point (x1, y1) to (x2, y2):
# - Horizontal distance = |x2 - x1|
# - Vertical distance   = |y2 - y1|
#
# In one second, a diagonal move reduces both distances by 1.
# So we should use diagonal moves as much as possible.
#
# The minimum time required is:
# max(|x2 - x1|, |y2 - y1|)
#
# We compute this for every consecutive pair of points
# and sum it up to get the total minimum time.
#
# Time Complexity: O(n)
# Space Complexity: O(1)