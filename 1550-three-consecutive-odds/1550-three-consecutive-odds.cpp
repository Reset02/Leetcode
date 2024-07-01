class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int consecutive_odd = 0;

        for (int i = 0; i < arr.size(); i++){
            if (arr[i] % 2 != 0){
                consecutive_odd ++;
            }
            else{
                consecutive_odd = 0;
            }
            if (consecutive_odd == 3){
                return true;
            }
        }
        return false;
    }
};