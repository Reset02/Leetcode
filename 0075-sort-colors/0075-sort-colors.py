class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3
        for i in nums:
            freq[i] += 1
        
        count = 0
        for i in range(3):
            nums[count: count + freq[i]] = [i] * freq[i]
            count += freq[i]
        