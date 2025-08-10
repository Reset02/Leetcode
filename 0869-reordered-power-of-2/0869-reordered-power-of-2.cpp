class Solution {
public:
    string sort_digits(int x){
        string s = to_string(x);
        sort(s.begin(), s.end());
        return s;
    }

    bool reorderedPowerOf2(int n) {
        // 預先計算所有 2 的冪，並存成排序後字串
        unordered_set<string> powerSet;
        for (int i = 0; i < 31; ++i){// 2^30 < 10^9
            powerSet.insert(sort_digits(1 << i));
        }

        // 判斷 n 排序後的字串是否存在
        return powerSet.count(sort_digits(n)) > 0;
    }
};