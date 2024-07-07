class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int consumed_bottles = 0;

        while (numBottles >= numExchange){
            // Maximum number of times we can consume numExchange
            // number of bottles using numBottles.
            int k = numBottles / numExchange;

            consumed_bottles += numExchange * k;
            numBottles -= numExchange * k;

            numBottles += k;
        }
        return consumed_bottles + numBottles;
    }
};