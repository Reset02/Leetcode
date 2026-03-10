class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for c in nums1:
            count[c] = count.get(c, 0) + 1
        
        result = []
        
        for c in nums2:
            if c in count and count[c] > 0:
                result.append(c)
                count[c] -= 1
        
        return result