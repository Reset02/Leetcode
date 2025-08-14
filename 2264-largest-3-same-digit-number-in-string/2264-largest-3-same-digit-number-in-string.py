class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_good = ""
        for i in range(n - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                if sub > max_good:
                    max_good = sub
        return max_good
