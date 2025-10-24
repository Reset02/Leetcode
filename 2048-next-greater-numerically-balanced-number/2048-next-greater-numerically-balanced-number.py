class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # 從 n+1 開始往上找
        num = n + 1
        while True:
            s = str(num)
            count = Counter(s)
            # 檢查是否平衡
            if all(int(digit) == freq for digit, freq in count.items()):
                return num
            num += 1