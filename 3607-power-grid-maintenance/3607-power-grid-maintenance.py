from collections import defaultdict
import heapq

def powerGridMaintenance(c, connections, queries):
    # Step 1: 建立圖
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 2: DFS 找出所有連通分量
    comp_id = [0] * (c + 1)
    comp_nodes = defaultdict(list)
    comp_index = 0

    def dfs(u, cid):
        comp_id[u] = cid
        comp_nodes[cid].append(u)
        for v in graph[u]:
            if comp_id[v] == 0:
                dfs(v, cid)

    for i in range(1, c + 1):
        if comp_id[i] == 0:
            comp_index += 1
            dfs(i, comp_index)

    # Step 3: 為每個 component 建立 heap（初始全在線）
    comp_heap = {}
    for cid, nodes in comp_nodes.items():
        heap = nodes[:]
        heapq.heapify(heap)
        comp_heap[cid] = heap

    offline = set()
    res = []

    # Step 4: 處理查詢
    for typ, x in queries:
        if typ == 1:
            if x not in offline:
                res.append(x)
            else:
                cid = comp_id[x]
                heap = comp_heap[cid]
                # 移除堆中離線的節點
                while heap and heap[0] in offline:
                    heapq.heappop(heap)
                if heap:
                    res.append(heap[0])
                else:
                    res.append(-1)
        else:  # typ == 2
            offline.add(x)

    return res
