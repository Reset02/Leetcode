class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles # 一開始先把所有瓶子喝掉
        empty = numBottles # 喝完後都是空瓶

        while empty >= numExchange:
            newFull = empty // numExchange # 換到的新瓶
            ans += newFull # 喝掉
            empty = empty % numExchange + newFull # 更新空瓶數
        
        return ans