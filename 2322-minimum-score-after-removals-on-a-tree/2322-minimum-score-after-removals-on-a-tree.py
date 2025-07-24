class Solution:
    # 計算三個 XOR 結果的最大值與最小值差距
    def calc(self, a: int, b: int, c: int) -> int:
        return max(a, b, c) - min(a, b, c)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)                   # 節點數
        cnt = 0                         # 時間戳計數器
        sum_xor = [0] * n               # sum_xor[i]：以 i 為根的子樹 XOR 值
        tin = [0] * n                   # tin[i]：DFS 進入節點 i 的時間
        tout = [0] * n                  # tout[i]：DFS 離開節點 i 的時間
        adj = [[] for _ in range(n)]   # 建立鄰接表（無向圖）

        # 建立圖
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS 前處理：建立時間戳與子樹 XOR 值
        def dfs(x: int, parent: int):
            nonlocal cnt
            tin[x] = cnt
            cnt += 1
            sum_xor[x] = nums[x]  # 初始為自己的值
            for neighbor in adj[x]:
                if neighbor == parent:
                    continue
                dfs(neighbor, x)
                sum_xor[x] ^= sum_xor[neighbor]  # 把子樹 XOR 加進來
            tout[x] = cnt  # 記錄離開時間

        dfs(0, -1)  # 從根節點 0 開始 DFS

        res = float("inf")  # 最小結果初始化為無限大

        # 枚舉每對節點 (u, v)，模擬移除這兩個節點與其父邊
        for u in range(1, n):
            for v in range(u + 1, n):
                # Case 1: v 是 u 的子孫（v 在 u 的子樹中）
                if tin[v] > tin[u] and tin[v] < tout[u]:
                    # 三個部分為：
                    # A = 整棵樹 XOR u 子樹
                    # B = u 子樹 XOR v 子樹
                    # C = v 子樹
                    res = min(
                        res,
                        self.calc(
                            sum_xor[0] ^ sum_xor[u], # 區塊 A：整棵樹 - u 子樹
                            sum_xor[u] ^ sum_xor[v], # 區塊 B：u 子樹 - v 子樹
                            sum_xor[v],              # 區塊 C：v 子樹
                        ),
                    )
                # Case 2: u 是 v 的子孫（u 在 v 的子樹中）
                elif tin[u] > tin[v] and tin[u] < tout[v]:
                    res = min(
                        res,
                        self.calc(
                            sum_xor[0] ^ sum_xor[v],
                            sum_xor[v] ^ sum_xor[u],
                            sum_xor[u],
                        ),
                    )
                # Case 3: u 和 v 無交集（不在彼此子樹內）
                else:
                    res = min(
                        res,
                        self.calc(
                            sum_xor[0] ^ sum_xor[u] ^ sum_xor[v],
                            sum_xor[u],
                            sum_xor[v],
                        ),
                    )

        return res  # 回傳最小分數