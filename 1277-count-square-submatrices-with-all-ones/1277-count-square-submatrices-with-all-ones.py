class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m , n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1) # dp[j] 代表上一列計算後目前的 dp[i-1][j-1] 轉移結果
        ans = 0
        for i in range(1, m + 1):
            prev_diag = 0 # 這回合的「左上角」
            for j in range(1, n + 1):
                temp = dp[j] # 暫存上一列的 dp[j]，等下要變成下一格的左上角
                if matrix[i-1][j-1] == 1:
                    dp[j] = 1 + min(dp[j], dp[j-1], prev_diag)
                    ans += dp[j]
                else:
                    dp[j] = 0
                prev_diag = temp
        return ans