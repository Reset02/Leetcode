class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        possible = set()
        possible.add(word) # 原本沒出錯的情況

        i = 0
        while i < n:
            j = i
            # 找出一段連續相同的字元
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length >= 2:
                 # 嘗試刪除多餘的部分，只保留一個字元
                for k in range(1, length):
                    new_word = word[:i] + word[i+k:] # 刪掉 k 個重複字元
                    possible.add(new_word)
            i = j # 繼續下一段
        
        return len(possible)