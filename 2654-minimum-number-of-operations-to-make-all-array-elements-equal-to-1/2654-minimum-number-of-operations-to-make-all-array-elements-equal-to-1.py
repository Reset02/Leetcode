class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        total_gcd = reduce(gcd, nums)
        if total_gcd != 1:
            return -1
        
        # 若已有 1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # 沒有 1：找最短 gcd = 1 的子陣列
        min_len = float('inf')
        for i in range(n):
            cur_gcd = nums[i]
            for j in range(i + 1, n):
                cur_gcd = gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break # 不需繼續擴展此區段
        
        return (min_len - 1) + (n - 1)