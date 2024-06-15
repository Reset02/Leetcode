class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxheap = []
        i = 0
        for _ in range(k):
            # 檢查專案是否能夠以當前資本進行，如果可以，則將其可能的利潤（負值）加入最大堆 maxheap 中，並將索引 i 增加
            while i < n and projects[i][0] <= w: 
                heapq.heappush(maxheap, -projects[i][1])
                i += 1
            if not maxheap:
                break
            w -= heapq.heappop(maxheap)
        
        return w