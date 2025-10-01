class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles; // 一開始先喝掉所有瓶子
        int empty = numBottles; // 全部變成空瓶

        while (empty >= numExchange){
            int newFull = empty / numExchange; // 可以換的新瓶
            ans += newFull; // 喝掉這些新瓶
            empty = (empty % numExchange) + newFull; // 更新空瓶數
        }
        return ans;
    }
};