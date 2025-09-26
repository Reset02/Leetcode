class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int count = 0;

        // 固定最大邊 nums[k]
        for (int k = n - 1; k >= 2; k--){
            int i = 0, j = k - 1;
            while (i < j){
                if (nums[i] + nums[j] > nums[k]){
                    count += (j - i); // i 到 j-1 都成立
                    j--;
                } else{
                    i++;
                }
            }
        }
        return count;
    }
};