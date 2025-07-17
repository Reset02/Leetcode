class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 1  # 單個元素本身就是長度為 1 的合法子序列

        for num in nums:
            curr = num % k
            for prev in range(k):
                # 嘗試把 num 接在以 dp[curr][prev] 結尾的序列之後
                dp[prev][curr] = max(dp[prev][curr], dp[curr][prev] + 1)
                res = max(res, dp[prev][curr])

        return res