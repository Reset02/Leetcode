class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        prev_time = neededTime[0] # 前一個氣球的時間

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # 若相同，移除較小的那個
                total_time += min(prev_time, neededTime[i])
                # 保留花費時間較大的氣球
                prev_time = max(prev_time, neededTime[i])
            else:
                # 若不同，更新 prev_time
                prev_time = neededTime[i]
        
        return total_time