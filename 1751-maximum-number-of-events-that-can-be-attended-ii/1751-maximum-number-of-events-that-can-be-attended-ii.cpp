class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        
        // 排序事件依照 end time
        sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        // 把 end time 提出來做 binary search 用
        vector<int> ends;
        for (const auto& e : events) {
            ends.push_back(e[1]);
        }

        // dp[i][j]: 前 i 個事件中選 j 個的最大價值
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));

        for (int i = 1; i <= n; ++i) {
            int start = events[i - 1][0];
            int end = events[i - 1][1];
            int value = events[i - 1][2];

            // 找到不重疊的上一個事件（end < current start）
            int idx = upper_bound(ends.begin(), ends.end(), start - 1) - ends.begin();

            for (int j = 1; j <= k; ++j) {
                // 不選第 i 個事件
                dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                // 選第 i 個事件
                dp[i][j] = max(dp[i][j], dp[idx][j - 1] + value);
            }
        }

        return dp[n][k];
    }
};