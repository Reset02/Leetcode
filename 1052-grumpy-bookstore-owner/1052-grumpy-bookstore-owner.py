class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        # 基礎滿意度
        total_satisfied = 0
        for i in range(n):
            if not grumpy[i]:
                total_satisfied += customers[i]

        # 計算第一個窗口的增加值
        extra_satisfied = 0
        for i in range(minutes):
            if grumpy[i]:
                extra_satisfied += customers[i]
        
        max_extra_satisfied = extra_satisfied
        
        # 滑動窗口
        for i in range(minutes, n):
            if grumpy[i]:
                extra_satisfied += customers[i]
            if grumpy[i - minutes]:
                extra_satisfied -= customers[i - minutes]
            
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        # 最終結果
        return total_satisfied + max_extra_satisfied