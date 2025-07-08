import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1]) # 按照 endDay 排序
        n = len(events)
        ends = [e[1] for e in events]

        # dp[i][j]: 前 i 個事件，最多選 j 個的最大價值
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # 找不重疊的最後一個事件
            idx = bisect.bisect_right(ends, start - 1)
            for j in range(1, k + 1):
                # 不選第 i 個事件
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # 選第 i 個事件（從第 idx 個事件轉移）
                dp[i][j] = max(dp[i][j], dp[idx][j - 1] + value)
        
        return dp[n][k]