class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int total_time = 0;
        int prev_time = neededTime[0]; // 上一個氣球的時間

        for (int i = 1; i < colors.size(); i++){
            if (colors[i] == colors[i - 1]){
                // 若顏色相同 -> 移除花費時間較小的那一顆
                total_time += min(prev_time, neededTime[i]);
                // 保留花費時間較大的作為新的基準
                prev_time = max(prev_time, neededTime[i]);
            } else{
                // 若顏色不同 -> 更新基準時間
                prev_time = neededTime[i];
            }
        }
        return total_time;
    }
};