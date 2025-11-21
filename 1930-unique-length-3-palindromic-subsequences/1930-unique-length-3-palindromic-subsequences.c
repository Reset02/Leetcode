int countPalindromicSubsequence(char* s) {
    int n = strlen(s);

    int left[26], right[26];
    for (int i = 0; i < 26; i++){
        left[i] = -1;
        right[i] = -1;
    }

    // 找每個字元的最左與最右出現位置
    for (int i = 0; i < n; i++){
        int c = s[i] - 'a';
        if (left[c] == -1)
            left[c] = i;
        right[c] = i;
    }

    int ans = 0;
    // 對每一種字元 a 計算所有 a_b_a 的組合
    for (int c = 0; c < 26; c++){
        int l = left[c];
        int r = right[c];

        if (l != -1 && r != -1 && l < r){
            int seen[26] = {0}; // 記錄中間的字元
            for (int i = l + 1; i < r; i++){
                seen[s[i] - 'a'] = 1;
            }
            for (int i = 0; i < 26; i++){
                ans += seen[i];
            }
        }
    }
    return ans;
}