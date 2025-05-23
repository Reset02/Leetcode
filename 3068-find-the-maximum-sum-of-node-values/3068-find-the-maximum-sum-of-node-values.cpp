class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int n = nums.size(); // 節點數量
        
        vector<int> netChange(n);
        long long  nodeSum = 0;

        // 計算 netChange：每個節點 XOR k 後與原本的差值
        for (int i = 0; i < n; ++i) {
            netChange[i] = (nums[i] ^ k) - nums[i];
            nodeSum += nums[i]; // 初始總和
        }

        // 將變化量從大到小排序
        sort(netChange.begin(), netChange.end(), greater<int>());

        // 每次配對兩個，如果總提升值為正就加入總和
        for (int i = 0; i + 1 < n; i += 2) {
            int pairSum = netChange[i] + netChange[i + 1];
            if (pairSum > 0) {
                nodeSum += pairSum;
            }
        }

        return nodeSum; // 回傳最大總和
    }
};