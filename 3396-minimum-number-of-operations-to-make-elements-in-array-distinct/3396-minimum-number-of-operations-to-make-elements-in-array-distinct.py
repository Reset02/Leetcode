class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = [False] * 128  # 記錄 0~127 的數字是否出現過（題目約定數值範圍）

        for i in range(len(nums) - 1, -1, -1):  # 反向遍歷
            if seen[nums[i]]:  # 如果這個數字已經出現過
                return i // 3 + 1  # 算出最少需要幾次移除操作
            seen[nums[i]] = True  # 標記這個數字已出現過
        return 0