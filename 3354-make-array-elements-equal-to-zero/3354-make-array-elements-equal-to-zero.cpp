class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int count = 0; // 紀錄有效的 (起始點, 方向) 組合數量
        int nonZeros = 0; // 紀錄目前陣列中非零元素的數量
        int n = nums.size();

        // 計算初始陣列中有多少個非零元素
        for (int i = 0; i < n; i++){
            if (nums[i] > 0){
                nonZeros++;
            }
        }
        // 嘗試從每個 nums[i] == 0 的位置開始模擬
        for (int i = 0; i < n; i++){
            if (nums[i] == 0){
                // 嘗試往左移動的情況
                if (isVaild(nums, nonZeros, i, -1)){
                    count++;
                }
                // 嘗試往右移動的情況
                if (isVaild(nums, nonZeros, i, 1)){
                    count++;
                }
            }
        }
        return count; // 回傳總共多少個有效的起始設定
    }
private:
    // 判斷從某個起點與方向開始，是否能讓所有元素歸零
    bool isVaild(const vector<int>& nums, int nonZeros, int start, int direction){
        int n = nums.size();
        vector<int> temp(nums); // 建立陣列副本以便模擬，不影響原本 nums
        int curr = start;       // 當前位置指標

        // 當仍有非零元素，且 curr 在合法範圍內
        while (nonZeros > 0 && curr >= 0 && curr < n){
            if (temp[curr] > 0){    // 若當前元素 > 0
                temp[curr]--;       // 將該元素減 1
                direction *= -1;    // 反轉移動方向
                if (temp[curr] == 0){
                    nonZeros--; // 若該元素剛好變為 0，更新非零計數
                }
            }
            curr += direction;  // 根據當前方向移動到下一格
        }
        // 若所有元素最終都變為 0，則該起始條件有效
        return nonZeros == 0;
    }
};