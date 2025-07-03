class Solution:
    def kthCharacter(self, k: int) -> str:
        shift = 0  # 表示這個字元經歷了幾次 +1
        while k > 1:
            # 找目前這層字串的總長度為多少（最接近 k 的 2 的冪次）
            length = 1
            while length * 2 < k:
                length *= 2

            if k > length: # k 在後半段（+1 過後的字元）
                k -= length # 回推到原本對應的字元位置
                shift += 1 # 多加一次 +1
            else:
                # k 在前半段 → 原封不動只是來自前一層
                pass
        # 最後一定會回推到 k = 1，也就是初始字元 'a'
        # 根據 shift 次數決定字元變化（要注意 z 要循環回 a，所以 mod 26）
        return chr((shift % 26) + ord('a'))