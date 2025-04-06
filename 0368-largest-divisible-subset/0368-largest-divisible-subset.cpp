class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.empty()) return {};

        sort(nums.begin(), nums.end()); // 先排序
        int n = nums.size();

        vector<int> dp(n, 1); // 每個元素最長長度初始為 1
        vector<int> prev(n, -1); // 前一個元素索引，預設為 -1

        int max_len = 1;
        int max_idx = 0;

        for (int i = 1; i < n; ++i){
            for (int j = 0; j < i; ++j){
                if (nums[i] % nums[j] == 0){
                    if (dp[j] + 1 > dp[i]){
                        dp[i] = dp[j] + 1;
                        prev[i] = j;
                    }
                }
            }
            if (dp[i] > max_len){
                max_len = dp[i];
                max_idx = i;
            }
        }
        // 回溯構建答案
        vector<int> res;
        while (max_idx != -1){
            res.push_back(nums[max_idx]);
            max_idx = prev[max_idx];
        }
        reverse(res.begin(), res.end()); // 題目不要求順序，可加可不加
        return res;
    }
};