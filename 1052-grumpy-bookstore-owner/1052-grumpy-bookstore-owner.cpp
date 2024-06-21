class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int n = customers.size();

        // 計算基礎滿意度
        int total_satisfied = 0;
        for (int i = 0; i < n; i++){
            if (!grumpy[i]){
                total_satisfied += customers[i];
            }
        }

        // 計算第一個窗口的增加值
        int extra_satisfied = 0;
        for (int i = 0; i < minutes; i++){
            if (grumpy[i]){
                extra_satisfied += customers[i];
            }
        }

        int max_extra_satisfied = extra_satisfied;

        // 滑動窗口
        for (int i = minutes; i < n; i++){
            if (grumpy[i]){
                extra_satisfied += customers[i];
            }
            if (grumpy[i - minutes]){
                extra_satisfied -= customers[i - minutes];
            }
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied);
        }
        return total_satisfied + max_extra_satisfied;
    }
};