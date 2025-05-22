class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # 先將 queries 按照起始位置 l 進行排序，方便後續線性掃描時加入 heap
        queries.sort(key=lambda x: x[0])

        heap = []  # 最大堆 (使用負號模擬最大堆)，每次優先選右端 r 最大的 query
        deltaArray = [0] * (len(nums) + 1)  # 差分陣列，代表每個位置的操作次數變化
        operations = 0  # 當前位置可用的操作次數
        j = 0  # 指向 queries 的 index

        for i, num in enumerate(nums):  # 逐一處理 nums 的每個位置
            operations += deltaArray[i]  # 將差分陣列的變化加進來，更新目前可用操作數

            # 將所有從 i 開始的 query 推進 heap
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])  # 推入負的 r，維持最大堆（r 越大越早被選）
                j += 1

            # 若目前對 nums[i] 的操作次數不足，就從 heap 中補充操作
            while operations < num and heap and -heap[0] >= i:
                operations += 1  # 使用一個操作（從一個 query 中借來）
                deltaArray[-heappop(heap) + 1] -= 1  # 該 query 的影響在 r+1 開始結束

            # 如果怎麼補都無法達到 nums[i] 的需求，代表失敗，直接回傳 -1
            if operations < num:
                return -1

        return len(heap)  # heap 中剩下的 queries 都是沒被使用的，可移除