class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def fast_pow(base, exp): # 快速冪演算法
            result = 1
            while exp > 0: # 當指數還沒變成 0，我們就持續做以下動作
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        even_positions = (n + 1) // 2  # 包含 index 0
        odd_positions = n // 2

        even_ways = fast_pow(5, even_positions)
        odd_ways = fast_pow(4, odd_positions)

        return (even_ways * odd_ways) % mod