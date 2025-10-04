class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            x = min(h[i], h[j])
            ans = max(ans, x * (j - i))
            if h[i] > h[j]:
                j -= 1
            else:
                i += 1
        return ans