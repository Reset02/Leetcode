class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 位元 AND 是一種只會讓值 越來越小或相等 的運算。
        # 所以，一個子陣列的 AND 不可能超過它裡面任何一個數字。
        # 那麼最大的 bitwise AND，一定是某個數字自己本身（最大數），或者連續的那幾個一樣的最大值。
        max_val = ans = current_streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans = current_streak = 0 # 遇到新的最大值就重置

            if max_val == num:
                current_streak += 1  # 累計連續最大值的長度
            else: 
                current_streak = 0 # 一遇到不是最大值就斷了

            ans = max(ans, current_streak) # 紀錄最長的連續最大值長度
        return ans