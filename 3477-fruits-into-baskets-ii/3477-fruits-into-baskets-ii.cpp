class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        vector<bool> used(n, false); // 記錄每個籃子是否已被使用
        int unplaced = 0; // 統計無法放置的水果種類數量

        // 從左到右依序處理每一種水果
        for (int i = 0; i < n; ++i) {
            bool placed = false; // 記錄當前水果是否已成功放入籃子

            // 從左到右尋找第一個容量足夠且尚未使用的籃子
            for (int j = 0; j < n; ++j) {
                if (!used[j] && baskets[j] >= fruits[i]) {
                    used[j] = true; // 標記籃子已被使用
                    placed = true;  // 成功放置
                    break;          // 找到就跳出
                }
            }

            // 如果沒有任何籃子可以放這個水果
            if (!placed) {
                unplaced++;
            }
        }

        return unplaced;
    }
};