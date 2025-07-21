class Solution {
public:
    string makeFancyString(string s) {
        string res;
        res.reserve(s.size()); // 使用 reserve 提前配置記憶體（優化效能)

        for(char c: s){
            int n = res.size();
            // 如果 res 已有至少兩個字元，且最後兩個字元都等於 c，
            // 就跳過這個字元（以避免出現三連字）
            if (n >= 2 && res[n - 1] == c && res[n - 2] == c){
                continue;
            }
            res.push_back(c);
        }
        return res;
    }
};