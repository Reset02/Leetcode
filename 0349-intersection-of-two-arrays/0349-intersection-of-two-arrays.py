class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = []

        for c in set(nums2):
            if c in seen:
                result.append(c)
        return result
