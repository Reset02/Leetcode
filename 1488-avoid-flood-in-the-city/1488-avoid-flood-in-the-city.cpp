class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        vector<int> ans(n, 1);
        unordered_map<int, int> lake_day; // lake -> 上次下雨的日子
        set<int> dry_days; // 可用乾旱的日子（升序）

        for (int i = 0; i < n; ++i){
            int lake = rains[i];
            if (lake > 0){
                ans[i] = -1;
                // 如果這個湖之前下過雨
                if (lake_day.count(lake)){
                    int prev_day = lake_day[lake];
                    // 找出第一個比 prev_day 大的乾旱日
                    auto it = dry_days.upper_bound(prev_day);
                    if (it == dry_days.end()){
                        return {}; // 無法避免洪水
                    }
                    int dry_day = *it;
                    ans[dry_day] = lake;    // 乾這個湖
                    dry_days.erase(it); // 從可用乾旱日中移除
                }
                lake_day[lake] = i;
            } else{
                // 沒下雨，這天可用來乾湖
                dry_days.insert(i);
            }
        }
        return ans;
    }
};