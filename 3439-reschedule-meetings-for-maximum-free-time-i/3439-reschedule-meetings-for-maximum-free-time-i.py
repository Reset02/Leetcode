class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        res = 0 # 儲存目前找到的最大空閒時間
        total = [0] * (n + 1) # 建立一個前綴和陣列 total[i] 表示前i個會議的總時長
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]

        for i in range(k - 1, n): # 滑動視窗的右邊界，視窗大小為 k，從 k-1 到 n-1。
            right = eventTime if i == n - 1 else startTime[i + 1] #若 i 是最後一個會議，那壓縮完後空間的右界為 eventTime。 否則，右界就是下一場會議的開始時間（不能撞到它）。
            left = 0 if i == k - 1 else endTime[i - k]

            # right - left: 是這段區間的總可用時間（視窗可壓縮的位置）。
            # total[i + 1] - total[i - k + 1]: 是這 k 個會議的總長度。
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res