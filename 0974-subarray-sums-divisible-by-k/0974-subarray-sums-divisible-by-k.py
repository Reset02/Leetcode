class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_mod = 0
        result = 0

        # 有 k 個餘數群組，從 0 到 k-1
        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            # 為了避免負餘數，取兩次模
            prefix_mod = (prefix_mod + num % k + k) % k
            # 加上具有相同餘數的子數組數量來抵消餘數
            result += modGroups[prefix_mod]
            modGroups[prefix_mod] += 1

        return result