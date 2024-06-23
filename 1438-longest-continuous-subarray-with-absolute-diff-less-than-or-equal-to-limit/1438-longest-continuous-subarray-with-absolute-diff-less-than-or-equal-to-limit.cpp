class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> maxDeque, minDeque;
        int left = 0, maxLength = 0;

        for (int right = 0; right < nums.size(); right++){
            // 更新最大值雙端隊列
            while (!maxDeque.empty() && nums[right] > maxDeque.back()){
                maxDeque.pop_back();
            }
            maxDeque.push_back(nums[right]);

            // 更新最小值雙端隊列
            while (!minDeque.empty() && nums[right] < minDeque.back()){
                minDeque.pop_back();
            }
            minDeque.push_back(nums[right]);

            // 檢查最大值和最小值的差值
            while (!maxDeque.empty() && !minDeque.empty() && maxDeque.front() - minDeque.front() > limit){
                if (nums[left] == maxDeque.front()){
                    maxDeque.pop_front();
                }
                if (nums[left] == minDeque.front()) {
                minDeque.pop_front();
                }
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};