class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int n = nums.size();
        int prefixMod = 0, result = 0;

        // 有 k 個餘數群組，從 0 到 k-1
        vector<int> modGroups(k);
        modGroups[0] = 1;
        
        for (int num: nums){
            // 為了避免負餘數，取兩次模
            prefixMod = (prefixMod + num % k + k) % k;
            // Add the count of subarrays that have the same remainder as the current
            // 加上具有相同餘數的子數組數量來抵消餘數
            result += modGroups[prefixMod];
            modGroups[prefixMod]++;
        }
        return result;
    }
};