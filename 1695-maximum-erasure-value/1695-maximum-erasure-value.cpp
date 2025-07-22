class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> seen;
        int left = 0, currentSum = 0, maxSum = 0;

        for(int right = 0; right < nums.size(); ++right){
            // 移除左邊直到不再有重複
            while (seen.count(nums[right])){
                seen.erase(nums[left]);
                currentSum -= nums[left];
                ++left;
            }
            // 加入新元素
            seen.insert(nums[right]);
            currentSum += nums[right];

            // 更新最大值
            maxSum = max(maxSum, currentSum);
        }
        return maxSum;
    }
};