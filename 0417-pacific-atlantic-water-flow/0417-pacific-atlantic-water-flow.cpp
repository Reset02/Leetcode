#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        vector<vector<int>> result;

        // 四個方向
        vector<pair<int, int>> dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};

        // 定義 DFS
        function<void(int,int,vector<vector<bool>>&)> dfs = [&](int r, int c, vector<vector<bool>>& visited) {
            visited[r][c] = true;
            for (auto [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                // 只往高度相等或更高的地方走（反向流入）
                if (!visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    dfs(nr, nc, visited);
                }
            }
        };

        // 太平洋邊界（上邊與左邊）
        for (int i = 0; i < m; i++) dfs(i, 0, pacific);
        for (int j = 0; j < n; j++) dfs(0, j, pacific);

        // 大西洋邊界（下邊與右邊）
        for (int i = 0; i < m; i++) dfs(i, n - 1, atlantic);
        for (int j = 0; j < n; j++) dfs(m - 1, j, atlantic);

        // 找交集
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        return result;
    }
};
