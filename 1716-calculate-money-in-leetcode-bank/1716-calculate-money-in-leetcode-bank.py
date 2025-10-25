class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # 完整週的總金額
        total = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2

        # 最後一週剩餘天數的金額
        for i in range(days):
            total += weeks + 1 + i
        
        return total