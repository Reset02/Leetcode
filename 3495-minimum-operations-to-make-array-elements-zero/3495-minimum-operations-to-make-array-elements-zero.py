class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # 計算 [1, x] 的總步數
        def totalSteps(x: int) -> int:
            if x <= 0:
                return 0
            steps_sum = 0
            # 每層區間: [4^k, 4^(k+1)-1]
            k = 0
            while (1 << (2*k)) <= x:  # 4^k = 2^(2k)
                left = 1 << (2*k)          # 4^k
                right = min(x, (1 << (2*(k+1))) - 1)  # min(x, 4^(k+1)-1)
                count = right - left + 1
                steps_sum += count * (k + 1)
                k += 1
            return steps_sum

        ans = 0
        for l, r in queries:
            total_steps = totalSteps(r) - totalSteps(l - 1)
            ans += (total_steps + 1) // 2
        return ans