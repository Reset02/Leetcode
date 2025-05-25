int longestPalindrome(char** words, int wordsSize) {
    int count[26][26] = {0}; // count[i][j] 表示字串 'a'+i, 'a'+j 出現的次數
    int length = 0;
    int has_center = 0;

    // 統計每個字串出現次數
    for (int i = 0; i < wordsSize; i++) {
        int a = words[i][0] - 'a';
        int b = words[i][1] - 'a';
        count[a][b]++;
    }

    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            if (i == j) {
                // 是回文字串（例如 "gg"）
                int pair = count[i][j] / 2;
                length += pair * 4;
                count[i][j] -= pair * 2;

                if (count[i][j] > 0) {
                    has_center = 1;
                }
            } else if (i < j) {
                // 配對 "ab" 和 "ba"
                int pair = count[i][j] < count[j][i] ? count[i][j] : count[j][i];
                length += pair * 4;
                count[i][j] -= pair;
                count[j][i] -= pair;
            }
        }
    }

    if (has_center) {
        length += 2; // 可以放中間的單一回文字串
    }

    return length;
    
}