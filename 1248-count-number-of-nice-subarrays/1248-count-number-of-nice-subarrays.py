class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        result = 0
        odd_count = 0

        for right in range(len(nums)):
            # 如果是奇數，更新 odd_count
            if nums[right] % 2 == 1:
                odd_count += 1
                count = 0

            # 當窗口中的奇數數量超過 k，移動左指針
            while odd_count == k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
                count += 1
            
            # 每當 odd_count 等於 k 時，count 就記錄了所有可能的子數組數量
            result += count

        return result