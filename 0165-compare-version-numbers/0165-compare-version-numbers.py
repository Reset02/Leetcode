class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 拆解字串 -> 轉成整數陣列
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        # 補齊長度
        n = max(len(v1), len(v2))
        v1 += [0] * (n - len(v1))
        v2 += [0] * (n - len(v2))
        
        # 逐項比較
        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0
