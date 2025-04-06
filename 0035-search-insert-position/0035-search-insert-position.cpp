class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // 二分搜尋 (Binary Search)
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high){
            int mid = low + (high - low) / 2;  // 計算中間位置
            if (nums[mid] == target){
                return mid;
            }else if (nums[mid] < target){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        // 如果未找到目標數字，返回應插入的位置
        return low;  // 這就是目標數字應該插入的位置
    }
};