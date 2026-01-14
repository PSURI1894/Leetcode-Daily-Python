# Question:
# You are given a 2D integer array squares where squares[i] = [xi, yi, li]
# represents a square with bottom-left corner (xi, yi) and side length li.
# All squares are axis-aligned.
#
# Find the minimum y-coordinate of a horizontal line such that
# the total area covered by squares above the line
# equals the total area covered by squares below the line.
#
# Important difference from Separate Squares I:
# - Overlapping areas must be counted ONLY ONCE.
#
# Answers within 1e-5 of the actual answer are accepted.


class Solution:
    def separateSquares(self, squares):
        # We sweep along the y-axis and track how the union-covered width changes.
        # This becomes a 1D "area balance" problem over y-intervals.

        events = []

        # Each square contributes a vertical interval [y, y+l]
        # Overlap handling is implicit via interval union on x.
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # square starts
            events.append((y + l, -1, x, x + l)) # square ends

        # Sort events by y
        events.sort()

        from bisect import insort, bisect_left

        active = []  # active x-intervals
        prev_y = events[0][0]
        total_area = 0.0
        slabs = []  # (y_start, y_end, slab_area)

        # Helper to compute union length of active x-intervals
        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            length = 0
            cur_start, cur_end = intervals[0]
            for s, e in intervals[1:]:
                if s > cur_end:
                    length += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            length += cur_end - cur_start
            return length

        i = 0
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                width = union_length(active)
                area = width * dy
                slabs.append((prev_y, y, area))
                total_area += area

            # Process all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1

            prev_y = y

        # We want the y where area below == area above
        target = total_area / 2.0
        acc = 0.0

        for y1, y2, area in slabs:
            if acc + area >= target:
                # interpolate within this slab
                width = area / (y2 - y1)
                return y1 + (target - acc) / width
            acc += area

        return slabs[-1][1]


# Explanation:
# This is significantly harder than Separate Squares I because overlaps
# must be counted only once (union area).
#
# Strategy:
# - Perform a vertical sweep line over y.
# - Track active x-intervals contributed by squares.
# - Between consecutive y-events, compute the union length of x-intervals.
# - This gives us rectangular "slabs" with known area.
#
# Once total union area is known:
# - We find the y where cumulative area below equals half of total area.
# - Interpolate inside the slab to get exact y.
#
# Why this works:
# - Union area changes only at square boundaries.
# - Between boundaries, area grows linearly.
#
# Time Complexity:
# O(n log n) due to sweep line and interval union
#
# Space Complexity:
# O(n)
