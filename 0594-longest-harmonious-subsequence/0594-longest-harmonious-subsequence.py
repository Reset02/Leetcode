class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_len = 0
        for num in counter:
            if num + 1 in counter:
                  max_len = max(max_len, counter[num] + counter[num + 1])
        
        return max_len
