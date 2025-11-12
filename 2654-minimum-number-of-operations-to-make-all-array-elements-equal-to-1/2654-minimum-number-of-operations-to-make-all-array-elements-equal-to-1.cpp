#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();

        // Step 1: 若整體 gcd > 1，無解
        int total_gcd = nums[0];
        for (int i = 1; i < n; ++i) {
            total_gcd = gcd(total_gcd, nums[i]);
        }
        if (total_gcd != 1)
            return -1;

        // Step 2: 若已有 1，直接計算非 1 元素個數
        int ones = count(nums.begin(), nums.end(), 1);
        if (ones > 0)
            return n - ones;

        // Step 3: 沒有 1 → 找最短 gcd = 1 的子陣列
        int minLen = INT_MAX;
        for (int i = 0; i < n; ++i) {
            int cur_gcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                cur_gcd = gcd(cur_gcd, nums[j]);
                if (cur_gcd == 1) {
                    minLen = min(minLen, j - i + 1);
                    break;  // 再延伸也不會更短，直接跳出
                }
            }
        }

        // Step 4: 總操作數 = (L - 1) + (n - 1)
        return (minLen - 1) + (n - 1);
    }
};
