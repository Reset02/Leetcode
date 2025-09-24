class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []

        # 處理正負號
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)

        # 整數部分
        res.append(str(numerator // denominator))
        reminder = numerator % denominator
        if reminder == 0:
            return "".join(res)
        
        res.append(".")
        reminder_map = {}

        # 小數部分
        while reminder != 0:
            if reminder in reminder_map:
                idx = reminder_map[reminder]
                res.insert(idx, "(")
                res.append(")")
                break
            
            reminder_map[reminder] = len(res)
            reminder *= 10
            res.append(str(reminder // denominator))
            reminder %= denominator
        
        return "".join(res)