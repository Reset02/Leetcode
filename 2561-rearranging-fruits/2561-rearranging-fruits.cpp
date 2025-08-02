class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        int m = INT_MAX; // 用來儲存整體最小水果價格
        unordered_map<int, int> frequency_map;

        // 統計 basket1 中每個水果的數量，並找出最小值
        for (int b1 : basket1) {
            frequency_map[b1]++;
            m = min(m, b1);
        }

        // basket2 的水果做相反操作（-1），繼續更新最小值
        for (int b2 : basket2) {
            frequency_map[b2]--;
            m = min(m, b2);
        }

        vector<int> merge; // 儲存所有需要交換的水果價格

        for (auto [k, c] : frequency_map) {
            // 若某水果總數是奇數，代表無法對半分，回傳 -1
            if (c % 2 != 0) {
                return -1;
            }
            // 每種水果差異值的一半，就是需要交換的個數
            for (int i = 0; i < abs(c) / 2; ++i) {
                merge.push_back(k);
            }
        }

        // 使用 nth_element 找出中位數前的元素（不需完全排序）
        nth_element(merge.begin(), merge.begin() + merge.size() / 2, merge.end());

        // 對前半段的元素累加交換成本
        return accumulate(
            merge.begin(), merge.begin() + merge.size() / 2, 0ll,  // 初始為 0ll (long long)
            [&](long long res, int x) -> long long {
                return res + min(2 * m, x);  // 直接交換或用兩次最便宜水果 m
            }
        );
    }
};
