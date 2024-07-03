class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() <= 4) {
            return 0;  // 如果數組長度不超過4，最多進行3次操作後，所有元素都可以相同
        }

        sort(nums.begin(), nums.end());  // 將數組排序

        // 計算四種情況的範圍
        int result = min({
            nums[nums.size() - 1] - nums[3],  // 最大的四個數移動到第三大的位置
            nums[nums.size() - 2] - nums[2],  // 最大的三個數移動到第二大的位置
            nums[nums.size() - 3] - nums[1],  // 最大的兩個數移動到第二小的位置
            nums[nums.size() - 4] - nums[0]   // 最大的數移動到最小的位置
        });
        return result;
    }
};