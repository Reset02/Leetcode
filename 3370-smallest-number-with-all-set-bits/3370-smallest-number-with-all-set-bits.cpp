class Solution {
public:
    int smallestNumber(int n) {
        long long k = 1;
        while ((1LL << k) - 1 < n){
            k++;
        }
        return (1LL << k) - 1;
    }
};