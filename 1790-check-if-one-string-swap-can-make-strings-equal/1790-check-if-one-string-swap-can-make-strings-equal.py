class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        s1_frequency_map = [0] * 26
        s2_frequency_map = [0] * 26
        num_diff = 0

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            if s1_char != s2_char:
                num_diff += 1
                # 如果不同的字母數超過 2，則無法透過一次交換讓兩個字串相等

                if num_diff > 2:
                    return False
        
            # increment frequencies
            s1_frequency_map[ord(s1_char) - ord('a')] += 1
            s2_frequency_map[ord(s2_char) - ord('a')] += 1

        # check if frequencies are equal
        return s1_frequency_map == s2_frequency_map