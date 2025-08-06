class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)  # 籃子總數
        m = int(math.sqrt(n))  # 分塊的大小（√n）
        section = (n + m - 1) // m  # 區塊總數，向上取整確保包含所有籃子

        count = 0  # 統計無法放置的水果種類數量
        maxV = [0] * section  # 每個區塊的最大值（籃子容量）

        # 初始化：為每個區塊計算最大籃子容量
        for i in range(n):
            block_id = i // m  # 籃子 i 屬於哪一個區塊
            maxV[block_id] = max(maxV[block_id], baskets[i])

        # 遍歷每種水果
        for fruit in fruits:
            unset = 1  # 記錄這個水果是否未被放置（預設未放置）
            
            # 從左至右檢查每個區塊，找是否有符合條件的籃子
            for sec in range(section):
                if maxV[sec] < fruit:
                    # 如果這個區塊內的最大籃子都裝不下這顆水果，就跳過
                    continue

                # 找到有可能放入的區塊，開始在這個區塊內找具體籃子
                choose = 0  # 紀錄是否找到可以放水果的籃子
                maxV[sec] = 0  # 重置此區塊最大值，等會重新更新
                for i in range(m):
                    pos = sec * m + i  # 區塊內的第 i 個籃子實際位置
                    if pos < n:
                        if baskets[pos] >= fruit and not choose:
                            # 如果籃子容量夠放這個水果，且還沒選過
                            baskets[pos] = 0  # 放入後籃子容量設為 0（表示已使用）
                            choose = 1  # 記錄已放入
                        # 更新區塊最大值
                        maxV[sec] = max(maxV[sec], baskets[pos])

                # 如果成功放置，unset 設為 0，並結束搜尋
                unset = 0
                break

            # 如果這顆水果找不到任何合適籃子，count +1
            count += unset

        return count  # 回傳無法放置的水果種類總數