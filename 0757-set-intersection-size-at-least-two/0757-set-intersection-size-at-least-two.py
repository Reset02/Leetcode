class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 1. Sort by end asc, start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # p1: last chosen point
        # p2: second last chosen point
        p1 = -1
        p2 = -1
        ans = 0

        for s, e in intervals:
            # Case 1: already have ≥2 points in interval
            if p2 >= s:
                continue

            # Case 2: have 1 point in interval, need 1 more
            if p1 >= s:
                ans += 1
                p2 = p1
                p1 = e
            else:
                # Case 3: no points in interval, need 2 points
                ans += 2
                p2 = e - 1
                p1 = e

        return ans