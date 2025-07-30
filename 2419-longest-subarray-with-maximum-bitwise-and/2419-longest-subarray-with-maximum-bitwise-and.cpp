class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int max_val = 0;
        int ans = 0, current_streak = 0;

        for (int num : nums){
            if (num > max_val){
                max_val = num;
                ans = 0;
                current_streak = 0;
            }
            if (num == max_val){
                current_streak++;
                ans = max(ans, current_streak);
            } else{
                current_streak = 0;
            }
        }
        return ans;
    }
};