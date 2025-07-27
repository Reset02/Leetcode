class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # 步驟一：先消除連續的重複數值
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        # 步驟二：遍歷中間元素，檢查是否為 hill 或 valley
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1 # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1 # Valley
        
        return count