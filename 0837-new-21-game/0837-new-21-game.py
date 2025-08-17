class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        
        # dp[i] = 當前分數為 i，最終得分 ≤ n 的機率
        dp = [0.0] * (k + maxPts)
        # 終止區間：已停止時是否 ≤ n
        for i in range(k, min(n, k + maxPts - 1) + 1):
            dp[i] = 1.0

        # 初始滑動和 S = sum(dp[k ... k+maxPts-1])
        S = sum(dp[k : k + maxPts])

        
        # 逆推 dp[i]
        for i in range(k - 1, -1, -1):
            dp[i] = S / maxPts
            S += dp[i] - dp[i + maxPts]# 更新滑動視窗

        return dp[0]
