class Solution {
public:
    const int MOD = 1e9 + 7;
    int possibleStringCount(string word, int k) {
        if (word.empty()) return 0;

        // Step 1: Run-Length Encoding，統計每段相同字元的長度
        vector<int> groups;
        int count = 1;
        for (int i = 1; i < word.length(); ++i) {
            if (word[i] == word[i - 1]) {
                ++count;
            } else {
                groups.push_back(count);
                count = 1;
            }
        }
        groups.push_back(count);  // 加入最後一段的統計數

        // Step 2: 計算每段可能對應原始字元的位置總乘積
        long long total = 1;
        for (int num : groups) {
            total = (total * num) % MOD;
        }

        if (k <= groups.size()) return total; // 若 group 數已達 k，直接回傳 total

        // Step 3: 動態規劃 - 計算「非法的原始字串組合」（長度 < k）
        vector<long long> dp(k, 0);
        dp[0] = 1;  // 長度為 0 的唯一組合是空字串

        for (int num : groups) {
            vector<long long> new_dp(k, 0);
            long long sum_val = 0;
            for (int s = 0; s < k; ++s) {
                if (s > 0) {
                    sum_val = (sum_val + dp[s - 1]) % MOD;
                }
                if (s > num) {
                    sum_val = (sum_val - dp[s - num - 1] + MOD) % MOD;
                }
                new_dp[s] = sum_val;
            }
            dp = new_dp;
        }

        // 統計非法原始組合（長度 < k 且 ≥ group 數）
        long long invalid = 0;
        for (int i = groups.size(); i < k; ++i) {
            invalid = (invalid + dp[i]) % MOD;
        }

        // 回傳合法組合數：total - invalid
        return (total - invalid + MOD) % MOD;
    }
};