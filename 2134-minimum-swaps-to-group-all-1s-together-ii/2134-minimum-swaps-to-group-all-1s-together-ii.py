class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 初始化最小交換次數為無窮大
        minimum_swaps = float("inf")
        
        # 計算數組中 1 的總數 使用 sum 函數計算 nums 中所有 1 的個數，這個值用來決定我們滑動窗口的大小。
        total_ones = sum(nums)
        
        # 初始化當前窗口內 1 的個數
        # 初始情況下，窗口內只有一個元素，ones_count 為 nums 的第一個元素的值，end 指針初始化為 0。
        ones_count = nums[0]
        end = 0

        # 滑動窗口遍歷數組
        for start in range(len(nums)):
            # 調整當前窗口內 1 的個數，移除滑出窗口的元素
            # start 為滑動窗口的左邊界，當 start 不為 0 時，我們需要從 ones_count 中減去滑出窗口的元素。
            if start != 0:
                ones_count -= nums[start - 1]

            # 將窗口擴展至所需大小，總長度為 total_ones
            # 我們擴展窗口的右邊界直到窗口大小等於 total_ones。由於數組可能是環狀的，因此使用模運算 end % len(nums)。
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]
            
            # 更新最小交換次數
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)

        return minimum_swaps
