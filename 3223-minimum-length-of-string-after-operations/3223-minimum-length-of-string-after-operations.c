# define MAX_CHAR 256 // 假設字元範圍是 ASCII
int minimumLength(char* s) {
    // Step 1: 計算每個字元的出現次數
    int charFrequencyMap[256] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        // 條件 s[i] != '\0' 確保只遍歷到字串的結尾，因為在 C 字串中，結尾的 '\0' 表示字串的結束。
        charFrequencyMap[(unsigned char)s[i]]++;
        // (unsigned char) 確保索引值始終是非負整數，避免訪問陣列的負索引導致的未定義行為
    }

    // Step 2: 計算需要刪除的字元數
    int deleteCount = 0;
    for (int i = 0; i < 256; i++) {
        int frequency = charFrequencyMap[i];
        if (frequency > 0) {
            if (frequency % 2 == 1) {
                // 如果頻率是奇數，刪除所有但保留一個
                deleteCount += frequency - 1;
            } else {
                // 如果頻率是偶數，刪除所有但保留兩個
                deleteCount += frequency - 2;
            }
        }
    }
    // Step 3: 返回刪除後的最小長度
    return strlen(s) - deleteCount;
}
