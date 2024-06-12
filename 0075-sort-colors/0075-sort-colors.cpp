class Solution {
public:
    void sortColors(vector<int>& nums) {
        int freq[3] = {0};
        for (int i : nums){
            freq[i]++;
        }
        int n = nums.size(), count = 0;
        for (int i = 0; i < 3; i++){
            fill(nums.begin() + count, nums.begin() + count + freq[i], i);
            count += freq[i];
        }
    }
};