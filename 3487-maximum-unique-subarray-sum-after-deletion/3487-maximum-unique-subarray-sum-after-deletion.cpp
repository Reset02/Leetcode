class Solution {
public:
    int maxSum(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> hashSet;
        int total = 0;

        for (int i = 0; i < n; ++i){
            if (hashSet.count(nums[i]) || nums[i] <= 0){
                continue;
            }
            total += nums[i];
            hashSet.insert(nums[i]);
        }
        
        if (total == 0 && n > 0){
            total = *std::max_element(nums.begin(), nums.end());
        }
        return total;
    }
};