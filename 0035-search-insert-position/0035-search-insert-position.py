class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分搜尋 (Binary Search)
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2  # 計算中間位置

            if nums[mid] == target:  # 找到目標數字
                return mid
            elif nums[mid] < target:  # 目標數字比中間的數字大
                low = mid + 1  # 調整低指針，排除中間值的左側區域
            else:  # 目標數字比中間的數字小
                high = mid - 1  # 調整高指針，排除中間值的右側區域

        # 如果未找到目標數字，返回應插入的位置
        return low  # 這就是目標數字應該插入的位置