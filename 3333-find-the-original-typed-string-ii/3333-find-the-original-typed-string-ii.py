class Solution:
    MOD = 10**9 + 7  # 題目要求的模數，避免整數溢位

    def possibleStringCount(self, word: str, k: int) -> int:
        if not word:
            return 0  # 若輸入為空字串，沒有任何可能原始字串

        # Step 1: 將字串進行 Run-Length Encoding，統計每段相同字元的長度
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # 加入最後一段的統計數

        # Step 2: 計算每段可能對應原始字元的位置總乘積（初步估算）
        total = 1
        for num in groups:
            total = (total * num) % self.MOD
            # 每段長度為 num，可能對應 num 種原始輸入（因為最少按一下，最多按 num 次）

        # 若目前 group 數就已達 k，代表原始長度一定合法，直接回傳 total
        if k <= len(groups):
            return total

        # Step 3: 動態規劃 - 計算「非法的原始字串組合」（長度 < k）
        dp = [0] * k
        dp[0] = 1  # 長度為 0 的唯一組合是空字串

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp  # 更新 dp 為處理完目前 group 後的結果

        # 統計長度 < k 的非法原始字串總數（從 len(groups) 開始因為每個 group 至少對應一個原始字元）
        invalid = sum(dp[len(groups):k]) % self.MOD

        # 最終答案：合法的組合 = total - invalid（注意加上 MOD 是為了避免負數）
        return (total - invalid + self.MOD) % self.MOD