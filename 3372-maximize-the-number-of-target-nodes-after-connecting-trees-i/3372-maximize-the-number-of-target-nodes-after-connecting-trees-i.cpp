#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    // DFS 遞迴：計算從 node 出發，在距離 k 內可以 reach 到幾個節點（包含自己）
    int dfs(int node, int parent, vector<vector<int>>& children, int k) {
        if (k < 0) return 0;  // 超出距離範圍

        int res = 1;  // 包含自己
        for (int child : children[node]) {
            if (child == parent) continue;  // 避免走回來
            res += dfs(child, node, children, k - 1);  // 繼續往下遞迴
        }
        return res;
    }

    // 建立圖並計算每個節點在距離 <= k 內可以 reach 到的節點數量
    vector<int> build(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        vector<vector<int>> children(n);  // 鄰接表
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            children[u].push_back(v);
            children[v].push_back(u);
        }

        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            res[i] = dfs(i, -1, children, k);
        }
        return res;
    }

    // 主函式：傳回每個第一棵樹的節點最大 target 數量
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n = edges1.size() + 1;

        // 計算第一棵樹中每個節點在距離 <= k 可以 reach 到的節點數
        vector<int> count1 = build(edges1, k);

        // 計算第二棵樹中每個節點在距離 <= k - 1 可以 reach 到的節點數
        vector<int> count2 = build(edges2, k - 1);

        // 找出第二棵樹中最大可達節點數
        int maxCount2 = *max_element(count2.begin(), count2.end());

        // 最終結果：第一棵樹中每個節點加上最大可能連接的節點數
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            res[i] = count1[i] + maxCount2;
        }
        return res;
    }
};
