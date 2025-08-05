class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)  # 取得水果與籃子的數量（題目說 fruits 與 baskets 長度相同）
        used = [False] * n  # 用來紀錄哪些籃子已經被使用過
        unplaced = 0  # 統計無法放置的水果種類數量

        # 從左到右依序處理每一種水果
        for fruit in fruits:
            placed = False  # 標記該水果是否已成功放入籃子

            # 從左到右找第一個還沒被用掉，且容量大於等於水果數量的籃子
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # 標記籃子已使用
                    placed = True  # 標記水果已放置
                    break  # 找到合適籃子後就跳出迴圈

            # 如果整圈都找不到可用籃子，就累加未放置水果的數量
            if not placed:
                unplaced += 1

        return unplaced  # 回傳無法放置的水果種類數量