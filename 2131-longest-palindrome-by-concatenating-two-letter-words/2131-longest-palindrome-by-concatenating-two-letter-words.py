class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        has_center = False # 用來記錄是否有可以放在中間的字串
        
        for word in count:
            rev = word[::-1]
            if word != rev:
                if rev in count:
                    pair = min(count[word], count[rev])
                    length += pair * 4
                    # 將配對用掉，避免重複使用
                    count[word] -= pair
                    count[rev] -= pair
            else:
                # 自己就是回文（如 "gg"）
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
                if count[word] > 0:
                    has_center = True
        
        if has_center:
            length += 2  # 加一組可以放在中間的回文

        return length