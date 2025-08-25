#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        if (mat.empty() || mat[0].empty()) return {};

        int m = mat.size(), n = mat[0].size();
        vector<int> result;
        result.reserve(m * n);

        int i = 0, j = 0, dir = 1;  // dir = 1 → 往右上, dir = -1 → 往左下

        for (int k = 0; k < m * n; k++) {
            result.push_back(mat[i][j]);

            if (dir == 1) {  // 往右上
                if (j == n - 1) {      // 到了右邊界
                    i++;
                    dir = -1;
                } else if (i == 0) {   // 到了上邊界
                    j++;
                    dir = -1;
                } else {               // 正常往右上
                    i--;
                    j++;
                }
            } else {  // dir == -1 → 往左下
                if (i == m - 1) {      // 到了下邊界
                    j++;
                    dir = 1;
                } else if (j == 0) {   // 到了左邊界
                    i++;
                    dir = 1;
                } else {               // 正常往左下
                    i++;
                    j--;
                }
            }
        }
        return result;
    }
};
