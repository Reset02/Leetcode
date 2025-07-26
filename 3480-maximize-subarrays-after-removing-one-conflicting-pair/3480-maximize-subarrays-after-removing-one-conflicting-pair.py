class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # 初始化每個 a 的最小與次小衝突值 b
        bMin1 = [2**31 - 1] * (n + 1)  # bMin1[a] 是與 a 衝突的最小 b
        bMin2 = [2**31 - 1] * (n + 1)  # bMin2[a] 是與 a 衝突的次小 b
        
        # 處理每一組衝突對，記錄 bMin1 和 bMin2
        for pair in conflictingPairs:
            a = min(pair[0], pair[1])  # 保證 a < b
            b = max(pair[0], pair[1])
            # 更新最小值與次小值
            if bMin1[a] > b:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif bMin2[a] > b:
                bMin2[a] = b

        res = 0  # 尚未刪除任何衝突對時，總合法子陣列數
        ib1 = n  # 記錄目前有效區間內最小 bMin1 的對應位置（索引）
        b2 = 0x3FFFFFFF  # 非常大的整數，用來記錄掃描過程中的最小 b2
        delCount = [0] * (n + 1)  # delCount[i]：刪除位置 i 的主衝突對後可額外貢獻多少合法子陣列

        # 從尾巴往前掃描整個序列
        for i in range(n, 0, -1):
            # 若當前 i 的主衝突比 ib1 小，就更新 ib1（代表更大的可行區間）
            if bMin1[ib1] > bMin1[i]:
                b2 = min(b2, bMin1[ib1])  # 更新 b2 候選（舊的主衝突值）
                ib1 = i  # 更新主控制值
            else:
                b2 = min(b2, bMin1[i])  # 保留更小的 b 候選
            
            # 以 i 為起點，合法的結束位置最多只能到 bMin1[ib1] - 1
            # 所以子陣列數量為 (bMin1[ib1] - i)，但要保證不超過 n+1
            res += min(bMin1[ib1], n + 1) - i

            # 如果刪除了 ib1 對應的衝突對，那麼右界可以擴到 min(b2, bMin2[ib1])
            # 所以可以額外貢獻這些子陣列（這段是最精華的技巧）
            delCount[ib1] += (
                min(min(b2, bMin2[ib1]), n + 1) - min(bMin1[ib1], n + 1)
            )

        # 最終答案為不刪除時的合法子陣列 + 最多可額外貢獻的部分（刪一對衝突）
        return res + max(delCount)