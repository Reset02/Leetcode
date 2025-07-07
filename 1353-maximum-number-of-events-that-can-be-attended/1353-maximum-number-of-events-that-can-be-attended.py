class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() # 依照 startDay 排序
        min_heap = []
        day = 0
        i = 0
        n = len(events)
        res = 0

        while i < n or min_heap:
            # 若 heap 為空，跳到下一個活動的開始日
            if not min_heap:
                day = events[i][0]
            
            # 將所有今天開始的活動加入 heap
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # 移除所有已經過期的活動
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # 如果有可參加的活動，參加結束最早的那個
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
                day += 1
        return res