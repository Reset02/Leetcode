class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip = [0] * (n + 1)  # 我們需要額外的一個位置來處理翻轉區間的結束，這裡的 +1 是為了避免索引越界


        flip_count = 0  # 這個變數記錄當前的位置是否被翻轉過

        for i in range(n):
            flip_count ^= flip[i]  # 當前是否被翻轉過
            if nums[i] == flip_count:  # 如果nums[i]是0並且沒有被翻轉，或者nums[i]是1並且被翻轉過了
                if i + k > n:
                    return -1  # 無法翻轉，返回-1
                flips += 1
                flip_count ^= 1  # 標記這次翻轉
                flip[i + k] ^= 1  # 標記翻轉區間結束

        return flips
            