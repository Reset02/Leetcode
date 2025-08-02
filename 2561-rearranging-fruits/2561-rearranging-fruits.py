class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # 統計 basket1 和 basket2 中每個水果出現的次數
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)

        # 將兩邊加總，得到總共每種水果的數量
        total = freq1 + freq2

        # 若某種水果的總數是奇數，表示無法對半分給兩個籃子，回傳 -1
        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1
        
        # 建立兩個 list，用來記錄要從哪邊搬水果
        move_from_b1 = [] # basket1 多出來的水果
        move_from_b2 = [] # basket2 多出來的水果

        for fruit in total:
            # 計算 basket1 比 basket2 多幾個
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                # basket1 多的部分，需要移動到 basket2
                move_from_b1.extend([fruit] * (diff // 2))
            elif diff < 0:
                # basket2 多的部分，需要移動到 basket1
                move_from_b2.extend([fruit] * (-diff // 2))

        # 排序：為了讓交換成本最小
        move_from_b1.sort() # 選最便宜的水果從 basket1 移出去
        move_from_b2.sort(reverse=True) # 選最貴的水果從 basket2 移出去

        # 找出所有水果中最便宜的一個，若要透過第三水果間接交換時會用到
        min_val = min(basket1 + basket2)

        cost = 0 # 總交換成本
        # 將兩邊要交換的水果配對起來，逐一計算交換成本
        for a, b in zip(move_from_b1, move_from_b2):
            # 每次交換可以直接交換 a 和 b（成本 min(a, b)）
            # 或者繞一圈經過兩次最便宜水果（成本 2 * min_val）
            cost += min(min(a, b), 2 * min_val)

        return cost # 回傳最小總成本