class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == c and res[-2] == c: # 每次加入之前，檢查 res 的最後兩個字元是否都等於目前的字元
                continue
            res.append(c)
        return ''.join(res)