class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int left = 0;
        int count = 0;
        int result = 0;
        int odd_count = 0;

        for (int right = 0; right < nums.size(); right++){
            if (nums[right] % 2 == 1){
                odd_count++;
                count = 0;
            }
        
        
            while (odd_count == k){
                if (nums[left] % 2 == 1){
                    odd_count--;
                }
                left++;
                count++;
            }
            result += count;
        }
        return result;
    }
};