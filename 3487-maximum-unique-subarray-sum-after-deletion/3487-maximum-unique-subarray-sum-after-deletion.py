class Solution:
    def maxSum(self, nums: List[int]) -> int:
        N = len(nums)
        hashSet = set()
        total = 0 

        for i in range(N):
            if nums[i] in hashSet or nums[i] <= 0:
                continue
            total += nums[i]
            hashSet.add(nums[i])
        
        if total == 0 and N > 0:
            total = max(nums)
        
        return total
        