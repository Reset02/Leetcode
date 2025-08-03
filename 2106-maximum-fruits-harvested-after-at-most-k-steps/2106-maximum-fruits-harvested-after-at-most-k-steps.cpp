class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int left = 0, right = 0;
        int n = fruits.size();
        int total = 0; // 當前區間內的水果總數
        int ans = 0;   // 最終結果

        // 計算從 startPos 到 fruits[left][0] ~ fruits[right][0] 的最少步數
        auto step = [&](int left, int right) {
            if (fruits[right][0] <= startPos) {
                // 區間完全在 startPos 左邊，只需走到最左邊
                return startPos - fruits[left][0];
            } else if (fruits[left][0] >= startPos) {
                // 區間完全在 startPos 右邊，只需走到最右邊
                return fruits[right][0] - startPos;
            } else {
                // 區間跨越 startPos，需走左右兩端
                return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) +
                       (fruits[right][0] - fruits[left][0]);
            }
        };

        // 使用 sliding window 掃描 fruits
        while (right < n) {
            total += fruits[right][1]; // 累加右端水果數量

            // 當步數超出限制時，縮小左邊界
            while (left <= right && step(left, right) > k) {
                total -= fruits[left][1];
                left++;
            }

            ans = max(ans, total); // 更新最大值
            right++;               // 右邊界擴張
        }

        return ans;
    }
};