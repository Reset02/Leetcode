class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;

        for (int i = 0; i < numRows; ++i){
            vector<int> row(i + 1, 1);  // 建立長度 i+1，預設為 1 的列

            // 填中間的數值
            for (int j = 1; j < i; ++j){
                row[j] = res[i - 1][j - 1] + res[i - 1][j];
            }
            res.push_back(row); // 把這一列加入結果中
        }
        return res;
    }
};