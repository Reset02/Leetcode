class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []      # 單調遞增堆疊
        res = 0     # 操作次數
        for a in nums:
            # 若當前數字比堆疊頂還小，就把較大的彈出
            while s and s[-1] > a:
                s.pop()

            # 若是 0，不影響後續操作
            if a == 0:
                continue

            # 若堆疊空 或 目前值比堆疊頂大 → 代表出現新的高度層
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
