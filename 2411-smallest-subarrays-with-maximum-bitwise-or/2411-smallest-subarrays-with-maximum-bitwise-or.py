class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)  # 數列長度
        pos = [-1] * 31  # 紀錄每一個 bit 最後一次出現為 1 的位置（初始化為 -1）
        ans = [0] * n  # 存放每個位置的最短子陣列長度

        # 從右往左處理，每個位置 i 往右看哪些 bit 需要涵蓋
        for i in range(n - 1, -1, -1):
            j = i  # 子陣列的結束位置，初始為 i 自己

            # 檢查 0~30 位的 bit（因為最大為 2^31-1）
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    # 若第 bit 位是 0，我們需要看看右邊是否有人提供這個 bit
                    if pos[bit] != -1:
                        # 更新 j 為目前這個 bit 最後一次出現的 index
                        j = max(j, pos[bit])
                else:
                    # 如果第 bit 位是 1，記錄它的出現位置
                    pos[bit] = i

            # 計算從 i 開始，到 j 為止的子陣列長度
            ans[i] = j - i + 1

        return ans