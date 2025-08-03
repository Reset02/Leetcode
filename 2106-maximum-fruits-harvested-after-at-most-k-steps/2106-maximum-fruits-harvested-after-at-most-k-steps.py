class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 初始化左右指標、總和、答案
        left = 0
        right = 0
        n = len(fruits)
        total = 0 # 紀錄目前窗口內的水果總數
        ans = 0 # 紀錄目前找到的最大水果總數

        # 定義一個函數，用來計算從 startPos 走到 fruits[left][0] ~ fruits[right][0] 所需的最少步數
        def step(left: int, right: int) -> int:
            # 情況一：整個區間都在 startPos 的左邊]
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            # 情況二：整個區間都在 startPos 的右邊
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            # 情況三：跨越 startPos 左右兩邊，需來回走
            else:
                return(
                    min(
                        abs(startPos - fruits[right][0]), # 先去右邊再往左
                        abs(startPos - fruits[left][0]) # 或先去左邊再往右
                    )
                    + fruits[right][0] - fruits[left][0] # 區間的總距離
                )
        
        # 使用 sliding window：每次固定右邊界，逐步調整左邊界
        while right < n:
            # 加入右邊界的水果數量
            total += fruits[right][1]

            # 如果步數超過限制，就收回左邊界的水果，左邊界右移
            while left <= right and step(left, right) > k:
                total -= fruits[left][1]
                left += 1
            # 更新最大答案
            ans = max(ans, total)

            # 右邊界右移
            right += 1
            
        return ans