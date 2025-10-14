class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False

        # inc_start[i] = 從 i 開始的嚴格遞增序列的長度（包含 i）
        inc_start = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1
            else:
                inc_start[i] = 1

        # 檢查是否存在 i 使得 inc_start[i] >= k 且 inc_start[i+k] >= k
        for i in range(0, n - 2 * k + 1):
            if inc_start[i] >= k and inc_start[i + k] >= k:
                return True

        return False
