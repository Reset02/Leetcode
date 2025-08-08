class Solution:
    def soupServings(self, n: int) -> float:
        # 縮放為 25 mL 為單位
        N = math.ceil(n/25)
        # 常見的快速返回門檻（實務上常用）
        if N >= 200: # 200 * 25 = 5000 mL；也常見用 4800 -> 192 單位，這裡用 200 保守一點
            return 1.0

        @functools.lru_cache(None)
        def f(a: int, b: int) -> float:
            if a <= 0 and b <= 0: # 代表在同一回合兩種湯都被用完 → 回傳 0.5（題目要求同時用完算一半）。
                return 0.5
            if a <= 0: # A 先用完 → 回傳 1.0。
                return 1.0
            if b <= 0: # B 先用完 → 回傳 0.0。
                return 0.0
            # 四種操作（單位）
            return 0.25 * (
                f(a - 4, b) +
                f(a - 3, b - 1) +
                f(a - 2, b - 2) +
                f(a - 1, b - 3)
            ) 
            # (4, 0) — pour 100 A, 0 B

            # (3, 1) — pour 75 A, 25 B

            # (2, 2) — pour 50 A, 50 B

            # (1, 3) — pour 25 A, 75 B

        return f(N, N)