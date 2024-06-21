class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 將位置排序
        position.sort()

        # 設置二分搜索的左右邊界 設置左右邊界：left為1（最小可能距離），right為position中最大值減去最小值（最大可能距離）。
        left, right = 1, position[-1] - position[0]    

        def canPlaceBalls(min_dist):
            # 使用貪心算法檢查是否可以在最小間距為 min_dist 的情況下放置所有球
            count, last_position = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        # 進行二分搜索
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid  # 如果可以放置，嘗試更大的間距
            else:
                right = mid - 1  # 如果不能放置，嘗試更小的間距
        
        return left