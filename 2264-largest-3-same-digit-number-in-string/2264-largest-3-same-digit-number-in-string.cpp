class Solution {
public:
    string largestGoodInteger(string num) {
        string max_good = "";
    for (int i = 0; i + 2 < (int)num.size(); ++i) {
        // 取長度為 3 的 substring
        string sub = num.substr(i, 3);
        // 判斷三位是否相同
        if (sub[0] == sub[1] && sub[1] == sub[2]) {
            if (sub > max_good) {
                max_good = sub;
            }
        }
    }
    return max_good;
    }
};