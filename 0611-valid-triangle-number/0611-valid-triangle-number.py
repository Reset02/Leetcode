class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, -1, -1): # 固定最大邊
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i) # 所有 i...j-1 都可以
                    j -= 1
                else:
                    i += 1
        return count