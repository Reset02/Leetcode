class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[1] = 1
        pref[1] = 1

        for i in range(2, n + 1):
            r = i - delay      # prefix 上界
            l = i - forget     # prefix 下界 (要用 pref[l])
            if r >= 1:
                left = pref[r]
                right = pref[l] if l >= 0 else 0
                dp[i] = (left - right) % MOD
            else:
                dp[i] = 0
            pref[i] = (pref[i-1] + dp[i]) % MOD

        # 最終答案：在第 n 天仍記得的人
        ans = (pref[n] - (pref[n - forget] if n - forget >= 0 else 0)) % MOD
        return ans