class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        // 從最後一位開始進行加一
        for (int i = n - 1; i >=0; --i){
            if (digits[i] < 9){
                digits[i]++;  // 如果當前位數小於 9，直接加一並返回
                return digits;
            }
            digits[i] = 0;// 如果當前位數為 9，則進位，將其設為 0
        }
        // 如果進位到了最高位，需要新增一位數字 1
        vector<int> result = {1};// 創建一個新數字 1
        result.insert(result.end(), digits.begin(), digits.end());
        return result;
    }
};