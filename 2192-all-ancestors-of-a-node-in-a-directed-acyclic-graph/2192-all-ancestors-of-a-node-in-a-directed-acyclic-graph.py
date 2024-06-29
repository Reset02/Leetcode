class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: 建立圖的鄰接表表示和入度表
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # graph[u].append(v): 將邊 (u, v) 添加到圖中，表示從節點 u 指向節點 v。
        # in_degree[v] += 1: 將節點 v 的入度增加1，表示有一條邊指向節點 v。
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: 拓撲排序
        topo_order = []
        # queue 是用來存放當前入度為0的節點的雙端隊列（deque）。我們首先將所有入度為0的節點加入隊列，這些節點是圖中的起點。
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft() # 從隊列的左側取出一個節點 node
            topo_order.append(node) # 將取出的節點加入 topo_order 列表中，這表示我們確定了這個節點在拓撲排序中的位置。
            for neighbor in graph[node]: # 遍歷從 node 出發的所有邊，對應的鄰接節點是 neighbor
                in_degree[neighbor] -= 1 # 將 neighbor 的入度減1，因為 node 已經被移除
                if in_degree[neighbor] == 0: # 如果 neighbor 的入度變為0，將其加入隊列，這意味著 neighbor 已經可以被處理。
                    queue.append(neighbor)

        # Step 3: 找出每個節點的所有祖先節點
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for neighbor in graph[node]:
                # 當訪問一個節點時，將當前節點的祖先節點集添加到其鄰接節點的祖先節點集中
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

        # 將結果轉換為列表格式並按要求返回
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result
        