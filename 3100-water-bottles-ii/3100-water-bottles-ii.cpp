class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int drank = 0;
        int full = numBottles;
        int empty = 0;

        while (full > 0 || empty >= numExchange){
            // 喝掉所有滿瓶
            drank += full;
            empty += full;
            full = 0;

            // 如果能換，就換一瓶
            if (empty >= numExchange){
                empty -= numExchange;
                full += 1;
                numExchange += 1;
            }
        }
        return drank;
    }
};