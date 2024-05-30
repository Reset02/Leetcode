class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 起始鎖組合為 '0000'
        start = '0000'
        # 將死亡組合轉換為集合，方便查找
        deadends = set(deadends)
        # 如果起始組合就是死亡組合或者目標組合是死亡組合，則無法解鎖，返回-1
        if start in deadends or target in deadends:
            return -1
        
        # 建立 BFS 用的佇列，將起始組合和步數（0步開始）加入佇列
        queue = deque([(start, 0)])
        # 設置已經訪問過的鎖組合，避免重複訪問
        visited = set(start)
        
        while queue:
            # 取出佇列中的組合和步數
            current, steps = queue.popleft()
            # 如果當前組合等於目標組合，則返回步數
            if current == target:
                return steps
            
            # 對當前組合的每個轉輪進行轉動，得到相鄰組合
            for i in range(4):
                # 向上轉動一位
                up = current[:i] + str((int(current[i]) + 1) % 10) + current[i+1:]
                # 向下轉動一位
                down = current[:i] + str((int(current[i]) - 1) % 10) + current[i+1:]
                
                # 如果相鄰組合不在死亡組合中且沒有訪問過，則加入佇列中並標記為已訪問
                if up not in deadends and up not in visited:
                    queue.append((up, steps + 1))
                    visited.add(up)
                if down not in deadends and down not in visited:
                    queue.append((down, steps + 1))
                    visited.add(down)
        
        # 如果無法解鎖，返回-1
        return -1