class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        
        # DFS：從 node 出發，往子節點遞迴，統計在距離 k 內可以訪問多少個節點（包含自己）
        def dfs(
            node: int, parent: int, children: List[List[int]], k: int
        ) -> int:
            if k < 0:
                return 0  # 距離超過 k，不能再往下遞迴
            res = 1  # 自己本身也算一個 target node
            for child in children[node]:
                if child == parent:
                    continue  # 避免走回父節點
                res += dfs(child, node, children, k - 1)  # 對每個子節點遞迴，距離減 1
            return res

        # 建樹與計算每個節點能 reach 到幾個節點（距離 <= k）
        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1  # 節點數等於邊數 + 1
            children = [[] for _ in range(n)]  # 建立鄰接表
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)  # 對每個節點做 DFS 統計可達節點數
            return res

        n = len(edges1) + 1  # 第一棵樹的節點數
        count1 = build(edges1, k)        # 計算每個節點在第一棵樹中距離 ≤ k 可達節點數
        count2 = build(edges2, k - 1)    # 第二棵樹距離上限是 k-1，因為會多一條邊連接到第一棵樹
        maxCount2 = max(count2)          # 第二棵樹中，任一節點作為連接點時最多可達節點數

        # 對第一棵樹中的每個節點 i，取其可達節點數 + 第二棵樹中最大可達數，即最大可能 target 數
        res = [count1[i] + maxCount2 for i in range(n)]
        return res
