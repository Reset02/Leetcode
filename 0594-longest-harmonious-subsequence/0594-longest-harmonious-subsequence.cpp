class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int>counter;
        int max_len = 0;

        // 統計每個數字的出現次數
        for(int num: nums){
            counter[num]++;
        }
        // 遍歷 map，尋找 num 和 num+1 是否都存在
        for (auto& [num, count]: counter){
            if (counter.find(num + 1) != counter.end()){
                max_len = max(max_len, count + counter[num + 1]);
            }
        }
        return max_len;
    }
};