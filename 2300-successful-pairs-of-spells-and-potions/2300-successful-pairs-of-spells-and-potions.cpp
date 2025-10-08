class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        int m = potions.size();
        vector<int> res;

        for(long long spell: spells){
            // threshold = success / spell (但要注意浮點誤差)
            long long threshold = (success + spell - 1) / spell; // ceiling division

            // 找到第一個 potion >= threshold
            auto it = lower_bound(potions.begin(), potions.end(), threshold);
            int idx = it - potions.begin();
            res.push_back(m - idx);
        }
        return res;
    }
};