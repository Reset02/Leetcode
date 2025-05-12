class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        std::set<int> nums; // 用來儲存不重複合法的數字
        int n = digits.size();

        // 三層迴圈列出所有不同 index 的排列
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j == i) continue;
                for (int k = 0; k < n; ++k) {
                    if (k == i || k == j) continue;

                    int a = digits[i], b = digits[j], c = digits[k];

                    // 第一位不能是 0，最後一位必須是偶數
                    if (a != 0 && c % 2 == 0) {
                        int num = a * 100 + b * 10 + c;
                        nums.insert(num);
                    }
                }
            }
        }

        // 將 set 轉成排序過的 vector 回傳
        return std::vector<int>(nums.begin(), nums.end());
    }
};