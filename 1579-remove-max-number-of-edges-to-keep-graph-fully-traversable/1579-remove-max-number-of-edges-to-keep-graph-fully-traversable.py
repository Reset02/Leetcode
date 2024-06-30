class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))  # 初始化每個節點的父節點為其自身
                self.rank = [1] * n  # 初始化每個節點的秩為 1

            def find(self, u):
                if self.parent[u] != u:
                    self.parent[u] = self.find(self.parent[u])  # 路徑壓縮
                return self.parent[u]

            def union(self, u, v):
                root_u = self.find(u)
                root_v = self.find(v)
                if root_u != root_v:
                    if self.rank[root_u] > self.rank[root_v]:
                        self.parent[root_v] = root_u  # 將秩較小的樹合併到秩較大的樹
                    elif self.rank[root_u] < self.rank[root_v]:
                        self.parent[root_u] = root_v
                    else:
                        self.parent[root_v] = root_u
                        self.rank[root_u] += 1  # 若兩個樹的秩相同，合併後根節點的秩加 1
                    return True
                return False
                
        # Main function logic
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        
        # 將邊按類型排序，優先處理類型 3 的邊
        edges = sorted(edges, key=lambda x: -x[0])
        
        total_edges_used = 0  # 計算已使用的邊數
        
        # 處理類型 3 的邊（Alice 和 Bob 都能使用）
        for edge_type, u, v in edges:
            if edge_type == 3:
                if alice_uf.union(u - 1, v - 1):
                    bob_uf.union(u - 1, v - 1)
                    total_edges_used += 1

        # 處理類型 1 和類型 2 的邊
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice_uf.union(u - 1, v - 1):
                    total_edges_used += 1
            elif edge_type == 2:
                if bob_uf.union(u - 1, v - 1):
                    total_edges_used += 1

        # 檢查 Alice 和 Bob 的圖是否都完全連通
        if len({alice_uf.find(i) for i in range(n)}) > 1 or len({bob_uf.find(i) for i in range(n)}) > 1:
            return -1

        # 計算並返回可以移除的邊數
        return len(edges) - total_edges_used

        