class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long result = 0;  // 紀錄最後答案（所有 0 子陣列數量）
        long long count = 0;   // 紀錄當前連續 0 的數量

        for (int num : nums) {        // 遍歷整個陣列
            if (num == 0) {           // 如果遇到 0
                count += 1;           // 連續 0 的數量 +1
                result += count;      // 以當前 0 為結尾的零子陣列數量 = count
            } else {                  // 如果遇到非 0
                count = 0;            // 連續 0 中斷，重置 count
            }
        }

        return result;  // 回傳最後的總數量
    }
};
