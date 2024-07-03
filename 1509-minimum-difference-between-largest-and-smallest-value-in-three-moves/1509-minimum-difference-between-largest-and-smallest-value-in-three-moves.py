class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()  # 將數組排序

        # 計算四種情況的範圍
        result = min(
            nums[-1] - nums[3],  # 最大的四個數移動到第三大的位置
            nums[-2] - nums[2],  # 最大的三個數移動到第二大的位置
            nums[-3] - nums[1],  # 最大的兩個數移動到第二小的位置
            nums[-4] - nums[0]   # 最大的數移動到最小的位置
        )

        return result
        