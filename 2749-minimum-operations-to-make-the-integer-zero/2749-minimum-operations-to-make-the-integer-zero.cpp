class Solution {
public:
    int makeTheIntegerZero(long long num1, long long num2) {
        for (int t = 1; t <= 60; t++){
            long long S = num1 - t * num2;
            if (S < 0) continue;
            int bits = __builtin_popcountll(S); // S 的二進位 1 的個數
            if (bits <= t && t <= S){
                return t;
            }
        }
        return -1;
    }
};