class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        const int MOD = 1e9 + 7;
        vector<long long> dp(n + 1, 0);    // dp[i] = 第 i 天新知道秘密的人數
        vector<long long> pref(n + 1, 0);  // 前綴和

        dp[1] = 1;
        pref[1] = 1;

        for (int i = 2; i <= n; i++) {
            int r = i - delay;   // 可開始傳播的最晚天數
            int l = i - forget;  // 已經忘記的最早天數

            if (r >= 1) {
                long long left = pref[r];
                long long right = (l >= 0 ? pref[l] : 0);
                dp[i] = (left - right + MOD) % MOD;
            } else {
                dp[i] = 0;
            }
            pref[i] = (pref[i - 1] + dp[i]) % MOD;
        }

        long long ans = (pref[n] - (n - forget >= 0 ? pref[n - forget] : 0) + MOD) % MOD;
        return (int)ans;
    }
};