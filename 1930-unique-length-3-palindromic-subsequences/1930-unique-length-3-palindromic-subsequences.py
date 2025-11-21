class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        # 找每個字元的最左與最右出現位置
        left = {}
        right = {}

        for i, ch in enumerate(s):
            if ch not in left:
                left[ch] = i
            right[ch] = i
        
        ans = 0

        # 對每個字母 a 計算可能的 'a b a'
        for ch in left:
            l = left[ch]
            r = right[ch]
            if l < r: # 需至少兩個相同字元
                # 取得中間區間的不同字元即可
                mid_chars = set(s[l+1:r])
                ans += len(mid_chars)
        
        return ans