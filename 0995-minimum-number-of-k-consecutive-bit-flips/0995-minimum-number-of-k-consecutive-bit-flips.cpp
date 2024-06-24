class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        int flips = 0;
        std::vector<int> flip(n + 1, 0);  // 我們需要額外的一個位置來處理翻轉區間的結束，這裡的 +1 是為了避免索引越界
        int flip_count = 0;  // 這個變數記錄當前的位置是否被翻轉過

        for (int i = 0; i < n; ++i) {
            flip_count ^= flip[i];  // 當前是否被翻轉過
            if (nums[i] == flip_count) {  // 如果 nums[i] 是 0 並且沒有被翻轉，或者 nums[i] 是 1 並且被翻轉過了
                if (i + k > n) {
                    return -1;  // 無法翻轉，返回 -1
                }
                flips++;
                flip_count ^= 1;  // 標記這次翻轉
                flip[i + k] ^= 1;  // 標記翻轉區間結束
            }
        }

        return flips;
    }
};
