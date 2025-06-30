class Solution {
public:
    vector<string>res;

    void backtrack(string current, int left, int right, int n){
        // 當字串長度達到 2*n，加入結果
        if (current.length() == 2 * n){
            res.push_back(current);
            return;
        }
        // 還可以加左括號
        if (left < n){
            backtrack(current + "(", left + 1, right, n);
        }
        // 還可以加右括號（且不會造成不合法）
        if (right < left){
            backtrack(current + ")", left, right + 1, n);
        }
    }
    vector<string> generateParenthesis(int n) {
        res.clear();
        backtrack("", 0, 0, n);
        return res;
    }
};