class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        res = []
        for num, f in freq.items():
            if f == 1:
                res.append(num)
        
        return res