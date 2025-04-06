class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

    #（DP）
    # 先排序陣列，因為較小的數比較可能整除後面的數
    # 使用 動態規劃：
        # dp[i] 表示以 nums[i] 為結尾的「最大可整除子集長度」
        # prev[i] 記錄 dp[i] 是從哪個 index 轉移來的（幫助我們回溯答案）
    # 遍歷每一個 nums[i]，並往前看所有 j < i 的元素，如果 nums[i] % nums[j] == 0，就有機會接在 j 後面組成更長的序列
    # 記下最大長度的子集，最後反向回推即可。

        if not nums:
            return []

        nums.sort()  # 步驟 1：排序
        n = len(nums)
        dp = [1] * n        # 步驟 2：每個位置初始長度為 1
        prev = [-1] * n     # 記錄前一個元素 index

        max_len = 1
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # 回溯 reconstruct subset
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]

        return res[::-1]  # 反轉，因為我們是從後往前回溯的