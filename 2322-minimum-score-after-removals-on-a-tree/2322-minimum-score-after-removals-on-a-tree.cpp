class Solution {
public:
    // 計算三個 XOR 結果的最大值與最小值差距
    int calc(int a, int b, int c) {
        return max({a, b, c}) - min({a, b, c});
    }

    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<int> sum_xor(n);        // sum_xor[i]：以 i 為根的子樹 XOR 值
        vector<int> tin(n), tout(n);   // DFS 進入與離開時間
        vector<vector<int>> adj(n);    // 鄰接表
        int cnt = 0;                   // 時間戳計數器

        // 建立無向圖
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        // DFS 前處理：記錄每個節點的時間戳與子樹 XOR 值
        function<void(int, int)> dfs = [&](int x, int parent) {
            tin[x] = cnt++;
            sum_xor[x] = nums[x];  // 初始化為自己的值
            for (int neighbor : adj[x]) {
                if (neighbor == parent) continue;
                dfs(neighbor, x);
                sum_xor[x] ^= sum_xor[neighbor];  // 把子樹 XOR 累加
            }
            tout[x] = cnt;
        };

        dfs(0, -1);  // 從根節點開始 DFS

        int res = INT_MAX;

        // 枚舉每對節點 (u, v)，模擬移除兩條邊
        for (int u = 1; u < n; ++u) {
            for (int v = u + 1; v < n; ++v) {
                if (tin[v] > tin[u] && tin[v] < tout[u]) {
                    // Case 1: v 是 u 的子孫
                    res = min(res, calc(
                        sum_xor[0] ^ sum_xor[u],     // 區塊 A：整棵樹 - u 子樹
                        sum_xor[u] ^ sum_xor[v],     // 區塊 B：u 子樹 - v 子樹
                        sum_xor[v]                   // 區塊 C：v 子樹
                    ));
                }
                else if (tin[u] > tin[v] && tin[u] < tout[v]) {
                    // Case 2: u 是 v 的子孫
                    res = min(res, calc(
                        sum_xor[0] ^ sum_xor[v],
                        sum_xor[v] ^ sum_xor[u],
                        sum_xor[u]
                    ));
                }
                else {
                    // Case 3: u 與 v 無交集
                    res = min(res, calc(
                        sum_xor[0] ^ sum_xor[u] ^ sum_xor[v],
                        sum_xor[u],
                        sum_xor[v]
                    ));
                }
            }
        }

        return res;
    }
};