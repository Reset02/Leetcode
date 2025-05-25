class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        length = 0
        has_center = False

        for word in count:
            rev = word[::-1]
            if word != rev and word < rev:  # 確保每組只處理一次
                pair = min(count[word], count[rev])
                length += pair * 4
            elif word == rev:
                pair = count[word] // 2
                length += pair * 4
                if count[word] % 2 == 1:
                    has_center = True

        if has_center:
            length += 2

        return length
        