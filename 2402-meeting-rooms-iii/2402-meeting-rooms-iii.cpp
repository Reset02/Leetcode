class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        vector<int> ans(n, 0);
        vector<long long> times(n, 0); 
        sort(meetings.begin(), meetings.end());

        for (int i = 0; i < meetings.size(); i++){
            int start = meetings[i][0], end = meetings[i][1];
            bool flag = false;
            int minind = -1;
            long long val = 1e18;
            for (int j = 0; j < n; j++){
                if (times[j] < val) val = times[j], minind = j;
                if (times[j] <= start){
                    flag = true;
                    ans[j]++;
                    times[j] = end;
                    break;
                }
            }
            if (!flag){
                ans[minind]++;
                times[minind] += (1ll*(end - start)); //(1ll * (end - start)) 這一步是將整數 end - start 強制轉換為 long long 類型。 1ll 是一個 long long 型別的整數值。
            }
        }
        int maxi = -1, id = -1;
        for (int i = 0; i < n; i++){
            if (ans[i] > maxi) maxi = ans[i], id = i;
        }
        return id;
        
    }
};