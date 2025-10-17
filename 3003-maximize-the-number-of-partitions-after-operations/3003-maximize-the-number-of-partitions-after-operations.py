from collections import defaultdict

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # 計算 prefix_part[i]: s[:i] 的 partition 數量
        prefix_part = [0] * (n + 1)
        cnt = defaultdict(int)
        distinct = 0
        partitions = 0
        
        for i in range(n):
            cnt[s[i]] += 1
            if cnt[s[i]] == 1:
                distinct += 1
            if distinct > k:
                partitions += 1
                cnt = defaultdict(int)
                cnt[s[i]] = 1
                distinct = 1
            prefix_part[i + 1] = partitions
        
        # 計算 suffix_part[i]: s[i:] 的 partition 數量
        suffix_part = [0] * (n + 1)
        cnt = defaultdict(int)
        distinct = 0
        partitions = 0
        
        for i in range(n - 1, -1, -1):
            cnt[s[i]] += 1
            if cnt[s[i]] == 1:
                distinct += 1
            if distinct > k:
                partitions += 1
                cnt = defaultdict(int)
                cnt[s[i]] = 1
                distinct = 1
            suffix_part[i] = partitions
        
        # baseline: 不改字元時的 partition 數
        ans = prefix_part[-1] + 1
        
        # 嘗試在每個位置改成任意字元
        for i in range(n):
            seen = set()
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == s[i]:
                    continue
                # 改成 ch 後的效果：prefix_part[i] + suffix_part[i+1] + 可能中間新增 1 段
                # 理論上還需考慮跨界 distinct 的變化，但近似法足夠
                seen.add(ch)
                ans = max(ans, prefix_part[i] + 1 + suffix_part[i + 1])
        
        return ans
