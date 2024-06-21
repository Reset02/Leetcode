class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        // 將位置排序
        sort(position.begin(), position.end());

        // 設置二分搜索的左右邊界
        int left = 1;
        int right = position.back() - position[0];
        // 進行二分搜索
        while (left < right) {
            int mid = (left + right + 1) / 2; // 使用 (left + right + 1) // 2 向上取整
            if (canPlaceBalls(position, m, mid)) {
                left = mid;  // 如果可以放置，嘗試更大的間距
            } else {
                right = mid - 1;  // 如果不能放置，嘗試更小的間距
            }
        }
        return left;   
    }
private:
    bool canPlaceBalls(const vector<int>& position, int m, int min_dist) {
        int count = 1;
        int last_position = position[0];

        for (int i = 1; i < position.size(); ++i) {
            if (position[i] - last_position >= min_dist) {
                count++;
                last_position = position[i];
                if (count == m) {
                    return true;
                }
            }
        }
        return false;
    }
};