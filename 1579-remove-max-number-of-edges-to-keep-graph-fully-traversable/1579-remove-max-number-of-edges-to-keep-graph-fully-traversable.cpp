class UnionFind {
public:
    UnionFind(int n) : parent(n), rank(n, 1) {
        iota(parent.begin(), parent.end(), 0);  // 初始化每個節點的父節點為其自身
    }

    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);  // 路徑壓縮
        }
        return parent[u];
    }

    bool unionSets(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            if (rank[root_u] > rank[root_v]) {
                parent[root_v] = root_u;  // 將秩較小的樹合併到秩較大的樹
            } else if (rank[root_u] < rank[root_v]) {
                parent[root_u] = root_v;
            } else {
                parent[root_v] = root_u;
                rank[root_u] += 1;  // 若兩個樹的秩相同，合併後根節點的秩加 1
            }
            return true;
        }
        return false;
    }

private:
    vector<int> parent;
    vector<int> rank;
};
class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        UnionFind aliceUF(n), bobUF(n);
        
        // 將邊按類型排序，優先處理類型 3 的邊
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0];
        });
        
        int totalEdgesUsed = 0;  // 計算已使用的邊數
        
        // 處理類型 3 的邊（Alice 和 Bob 都能使用）
        for (const auto& edge : edges) {
            int edgeType = edge[0], u = edge[1] - 1, v = edge[2] - 1;
            if (edgeType == 3) {
                if (aliceUF.unionSets(u, v)) {
                    bobUF.unionSets(u, v);
                    totalEdgesUsed += 1;
                }
            }
        }

        // 處理類型 1 和類型 2 的邊
        for (const auto& edge : edges) {
            int edgeType = edge[0], u = edge[1] - 1, v = edge[2] - 1;
            if (edgeType == 1) {
                if (aliceUF.unionSets(u, v)) {
                    totalEdgesUsed += 1;
                }
            } else if (edgeType == 2) {
                if (bobUF.unionSets(u, v)) {
                    totalEdgesUsed += 1;
                }
            }
        }

        // 檢查 Alice 和 Bob 的圖是否都完全連通
        if (countConnectedComponents(aliceUF, n) > 1 || countConnectedComponents(bobUF, n) > 1) {
            return -1;
        }

        // 計算並返回可以移除的邊數
        return edges.size() - totalEdgesUsed;
    }

private:
    int countConnectedComponents(UnionFind& uf, int n) {
        unordered_set<int> uniqueComponents;
        for (int i = 0; i < n; ++i) {
            uniqueComponents.insert(uf.find(i));
        }
        return uniqueComponents.size();
    }
};