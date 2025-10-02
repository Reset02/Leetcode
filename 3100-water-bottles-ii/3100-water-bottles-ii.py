class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        full = numBottles
        empty = 0

        while full > 0 or empty >= numExchange:
            # 喝掉所有滿瓶
            drank += full
            empty += full
            full = 0
        
            # 如果能換，就換一瓶
            if empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1
        
        return drank