class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        // 計算每個城市的度數
        unordered_map<int, int> degree;
        for (const auto& road : roads) {
            degree[road[0]]++;
            degree[road[1]]++;
        }
        // 將城市按度數排序
        vector<pair<int, int>> cities;
        for (const auto& entry : degree) {
            cities.push_back({entry.second, entry.first});
        }
        sort(cities.rbegin(), cities.rend());

        // 分配重要性值
        vector<int> importance(n, 0);
        int current_importance = n;
        for (const auto& city : cities) {
            importance[city.second] = current_importance;
            current_importance--;
        }

        // 計算總重要性
        long long total_importance = 0;
        for (const auto& road : roads) {
            total_importance += importance[road[0]] + importance[road[1]];
        }

        return total_importance;
    }
};