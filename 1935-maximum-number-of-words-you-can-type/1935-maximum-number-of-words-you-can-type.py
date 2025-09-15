class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # 把 text 切成單字
        words = text.split()
        # 把壞掉的字母存成 set，方便快速查詢
        broken = set(brokenLetters)

        count = 0 # 記錄可以打出的單字數量

        # 檢查每個單字
        for word in words:
            # 如果單字內「沒有」任何壞掉字母 → 可輸入
            if not any(ch in broken for ch in word):
                count += 1
        
        return count