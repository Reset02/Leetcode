class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # 計算每個城市的度數
        degree = defaultdict(int)
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        # 按照度數對城市進行排序
        sorted_cities = sorted(degree.keys(), key=lambda x: degree[x], reverse=True)
        
        # 分配重要性值
        importance = [0] * n
        current_importance = n
        for city in sorted_cities:
            importance[city] = current_importance
            current_importance -= 1

        # 計算總重要性
        total_importance = 0
        for road in roads:
            total_importance += importance[road[0]] + importance[road[1]]
        
        return total_importance
        