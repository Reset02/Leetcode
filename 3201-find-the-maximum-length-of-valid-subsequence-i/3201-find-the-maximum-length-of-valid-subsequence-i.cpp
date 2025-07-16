class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int oddCount = 0;
        int evenCount = 0;

        for (int num : nums){
            if (num % 2 == 0){
                evenCount++;
            }else{
                oddCount++;
            }
        }

        // Case 1 & 2: 全奇 或 全偶
        int max_same = max(oddCount, evenCount);
        
        // Case 3: 奇偶交錯
        int max_alternating  = 1;
        int last_parity = nums[0] % 2;

        for(int i = 1; i < nums.size(); ++i){
            int current_parity = nums[i] % 2;
            if (current_parity != last_parity){
                max_alternating++;
                last_parity = current_parity;
            }
        }
        return max(max_same, max_alternating);
    }
};